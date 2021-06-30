#!/usr/bin/python3
print("content-type: text/html")
print()
import cgi
import subprocess
f=cgi.FieldStorage()
cmd=f.getvalue("x")
if "launch" in cmd: 
         if "pod" in cmd:  
                x=cmd.split('pod') 
                x1=x[-1].split(' ')
                o=subprocess.getoutput("kubectl --kubeconfig /usr/share/httpd/admin.conf run "+ x1[1] + " --image="+x1[-1])   
    
if "create" in cmd: 
         if "deployment" in cmd:  
                x=cmd.split('deployment')  
                x1=x[-1].split(' ')  
                o=subprocess.getoutput("kubectl --kubeconfig /usr/share/httpd/admin.conf create deployment "+ x1[1] + " --image="+x1[-1])      
if "expose" in cmd: 
        if "deployment" in cmd:  
                   x=cmd.split('deployment')
                   x1=x[-1].split(' ')  
                   o=subprocess.getoutput("kubectl --kubeconfig /usr/share/httpd/admin.conf expose deployment "+ x1[1] + " --image="+x1[-1])
if "scale" in cmd: 
        if "deployment" in cmd:  
                    x=cmd.split('deployment')  
                    x1=x[-1].split(' ')   
                    o=subprocess.getoutput("kubectl --kubeconfig  /usr/share/httpd/admin.conf scale deployment "+ x1[1] + " --replica="+x1[-1])
if "environment" in cmd:
        if "delete" in cmd:  
                    x=cmd.split('delete')  
                     x1=x[-1].split(' ')
                     o=subprocess.getoutput("kubectl --kubeconfig /usr/share/httpd/admin.conf delete svc "+ x1[1])])
if "delete" in cmd: 
        if "pod" in cmd:
                    x=cmd.split('pod')  
                    x1=x[-1].split(' ')  
                    o=subprocess.getoutput("kubectl --kubeconfig /usr/share/httpd/admin.conf delete pod "+ x1[1])
if "kubectl" in cmd:
o=subprocess.getoutput(cmd)
print(o)
