{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "debugpy",
      "request": "launch",
      "name": "Launch FastAPI App",
      "program": "${workspaceFolder}/app/main.py",
      "args": [],
      "console": "integratedTerminal",
      "envFile": "${workspaceFolder}/.env",
      "justMyCode": true,
      "autoReload": true
    }
  ],
  "inputs": [
    {
      "type": "promptString",
      "id": "programPath",
      "description": "Enter the path to the program you want to debug"
    }
  ]
}