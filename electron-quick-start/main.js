// Modules to control application life and create native browser window
const {app, BrowserWindow} = require('electron')
const path = require('path')
//module.exports = path;

function createWindow () {
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
      preload: path.join(__dirname, 'preload.js')

    }
  })

  // and load the index.html of the app.
  mainWindow.loadFile('gui.html')

  // Open the DevTools.
  // mainWindow.webContents.openDevTools()
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(createWindow)

// Quit when all windows are closed.
app.on('window-all-closed', function () {
  // On macOS it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== 'darwin') app.quit()
})

app.on('activate', function () {
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (BrowserWindow.getAllWindows().length === 0) createWindow()
})


// function detect_faces() {
//   document.getElementById("detect").value = "Hang on..."
//   //const python = require('python-shell')
//   //var paths = require('path')

//     var options = {
//       scriptPath : path.join(__dirname, '/../engine/'),
//       pythonPath : '/usr/bin/python3'
//     }

//   var face = new python("faces.py", options);

//   face.end(function(err, code, message) {
//     document.getElementById("detect").value = "Detect faces";
//   })
// }
// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.
