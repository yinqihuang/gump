#### set up ####
setwd(dirname(rstudioapi::getSourceEditorContext()$path))

library(tidyverse)
library(emmeans)

#### summary ####
df <- list.files(path = "/Users/yinqi/Downloads/04_analysis/data", pattern = "subInfo*", full.names = TRUE) %>% tibble(filename = .) %>%  mutate(file_contents = map(filename, ~read_csv(.))) %>% unnest() %>% select(age, gender, condition)
summary(df)
