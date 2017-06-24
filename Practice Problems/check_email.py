import imaplib
server=imaplib.IMAP4_SSL('imap.gmail.com',993)
uname='rahuldileep'
pasw='newBEGINNING108'
server.login(uname,pasw)
stat,cnt=server.select('INBOX')
stat,dta=server.fetch(cnt[0],'(UID BODY[TEXT])')
print(dta)
server.close()
server.logout()