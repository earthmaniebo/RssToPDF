import smtplib
import mimetypes
import email
import email.mime.application

def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message, pdf_file,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    
    # Create a text/plain message
    msg = email.mime.Multipart.MIMEMultipart()
    msg['Subject'] = 'Test PDF'
    msg['From'] = 'earthmaniebo@gmail.com'
    msg['To'] = 'earth@codesignate.com'

    # PDF attachment
    fp = open(pdf_file,'rb')
    att = email.mime.application.MIMEApplication(fp.read(), _subtype = "pdf")
    fp.close()
    att.add_header('Content-Disposition', 'attachment', filename = pdf_file)
    msg.attach(att)
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, msg.as_string())
    server.quit()
    return problems