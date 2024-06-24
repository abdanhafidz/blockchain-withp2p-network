import subprocess
import os
import platform

def open_terminal_and_run(command, close_on_finish=False):
    system = platform.system()
    if close_on_finish:
        command += "; exit"
    
    if system == 'Windows':
        if close_on_finish:
            subprocess.Popen(['start', 'cmd', '/c', command], shell=True)
        else:
            subprocess.Popen(['start', 'cmd', '/k', command], shell=True)
    elif system == 'Darwin':  # macOS
        if close_on_finish:
            subprocess.Popen(['osascript', '-e', f'tell application "Terminal" to do script "{command}"'])
        else:
            subprocess.Popen(['osascript', '-e', f'tell application "Terminal" to do script "{command}"'])
    else:  # Linux
        if close_on_finish:
            subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', command])
        else:
            subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', f'{command}; exec bash'])

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    
    main_script = os.path.join(path, "__main__.py")
    websocketserver_script = os.path.join(path, "__websocketserver__.py")
    websocketclient_script = os.path.join(path, "__websocketclient__.py")
    
    # Install requirements and close terminal after finishing
    open_terminal_and_run("pip install -r requirements.txt", close_on_finish=True)
    # Run scripts and keep terminal open
    open_terminal_and_run(f"python {main_script}")
    open_terminal_and_run(f"python {websocketserver_script}")
    open_terminal_and_run(f"python {websocketclient_script}")
