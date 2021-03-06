Sub CountWordsInASpecificHighlightColor()
    Dim objDoc As Document
    Dim objWord As Object
    Dim nHighlightedStatements As Long
    Dim keepCounting As Boolean
    Dim strHighlightColor As String
 
    Application.ScreenUpdating = False
    Set objDoc = ActiveDocument
    numHighlightedStatements = 0
    strHighlightColor = InputBox("Choose a Highlight colour (enter the value):" & vbNewLine & _
      vbTab & "Green" & vbTab & vbTab & "4" & vbNewLine & _
      vbTab & "Red" & vbTab & vbTab & "6" & vbNewLine & _
      vbTab & "Turquoise" & vbTab & vbTab & "3" & vbNewLine & _
      vbTab & "Yellow" & vbTab & vbTab & "7", "Pick Highlight Color")
 
    keepCounting = False
    For Each objWord In objDoc.Words
        If objWord.HighlightColorIndex = strHighlightColor Then
           If Not keepCounting Then
               nHighlightedStatements = nHighlightedStatements + 1
               keepCounting = True
           End If
        Else
             keepCounting = False
        End If
    Next objWord
