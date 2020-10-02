#### set up ####
setwd(dirname(rstudioapi::getSourceEditorContext()$path))

library(tidyverse)
library(igraph)
library(ggraph)

#### load data ####
## read intrusion file
df <- list.files(path = '/Users/yinqi/Downloads/intrusions', pattern = '*.csv', full.names = TRUE) %>% tibble(filename = .) %>% mutate(file_contents = map(filename, ~read_csv(.))) %>% unnest() %>% select(-filename,-X7,-X8,-X9,-X10,-X11,-X12,-X13,-X14,-X15,-X16)
## read condition file
cb <- list.files(path = '/Users/yinqi/Downloads', pattern = 'counterbalance', full.names = TRUE) %>% tibble(filename = .) %>% mutate(file_contents = map(filename, ~ read_csv(.))) %>% unnest() %>% mutate(filename = case_when(str_detect(filename, "counterbalance") ~ str_remove(filename, "Users(.*)/counterbalance")), filename = str_remove(filename, ".csv"), filename = str_remove(filename, "/")) %>% select(-imgStim) %>% rename(counterbalance = filename)
## merge dfs
df <- df %>% left_join(cb, by = c('counterbalance', 'trial'))
## remove text 
df <- subset(df, select = -c(subID,trial,counterbalance,testTime,intrusionText,lag,narrativeCross,cond))

#### chisq ####
tbl <- table(df)
result <- (chisq.test(tbl))
print(result)

#### arc ####
tbl <- as.data.frame(tbl)
tbl <- subset(tbl, Freq >= 100) #100 is arbitrary

## convert to igraph
mygraph <- graph_from_data_frame(tbl)
p1 <-  ggraph(mygraph, layout="linear") + geom_edge_arc(edge_colour="grey", edge_alpha=0.3, fold = TRUE, end_cap = circle(0.2, 'cm'), start_cap = circle(0.2, 'cm'), aes(width = Freq)) + geom_node_point(color="black", size=0.3) + geom_node_text(aes(label=name), size=3, color="black", nudge_y = -0.5) 
