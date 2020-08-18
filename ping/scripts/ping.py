def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import subprocess, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + host
    need_sh = False if  platform.system().lower()=="windows" else True

    # Ping
    return subprocess.call(args, shell=need_sh) == 0

# test call
print(ping("127.0.0.1"))

####################################################
import subprocess
import platform

def ping_ip(current_ip_address):
        try:
            output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower() == "windows" else 'c', current_ip_address ), shell=True, universal_newlines=True)
            if 'unreachable' in output:
                return False
            else:
                return True
        except Exception:
                return False

if __name__ == '__main__':
    current_ip_address = ['127.0.0.1', '10.64.25.35', '10.0.2.15', '192.168.56.101']
    for each in current_ip_address:
        if ping_ip(each):
            print(f"{each} is available")
        else:
            print(f"{each} is not available")
