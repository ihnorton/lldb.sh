import lldb
import subprocess

def sh(debugger, command, result, dict):
  lldb_cmd,shell_cmd = map(x->x.strip(), command.split("|"))

  interpreter = debugger.GetCommandInterpreter()
  res = lldb.SBCommandReturnObject()
  interpreter.HandleCommand(lldb_cmd, res)

  if not res.Succeeded():
      raise Exception("failed to execute lldb command!")
  if not res.GetOutput():
      return

  # Not sure what the underlying buffer is for HandleCommand, but
  # maybe some check/optim for really large output
  output = res.GetOutput().encode('UTF-8')
  proc = subprocess.Popen(shell_cmd, shell=True, stdin=subprocess.PIPE)
  try:
      out, errs = proc.communicate(output, timeout=1)
  except subprocess.TimeoutExpired:
      proc.kill()
      outs, errs = proc.communicate()

def __lldb_init_module (debugger, dict):
  # I'm sure there's a less hacky way to do this...
  interpreter = debugger.GetCommandInterpreter()
  interpreter.HandleCommand('command script delete sh', res)
  debugger.HandleCommand('command script add -f lldbsh.sh sh ')
