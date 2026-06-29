!macro preInit
  !ifndef BUILD_UNINSTALLER
    DetailPrint "Stopping cOde(n) backend before install/update..."
    nsExec::ExecToLog '%SYSTEMROOT%\System32\cmd.exe /c taskkill /IM "coden-server.exe" /T /F'
  !endif
!macroend
