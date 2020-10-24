import win32com.client
oOutlook = win32com.client.Dispatch("Outlook.Application")
appt = oOutlook.CreateItem(1) # 1 - olAppointmentItem
appt.Start = '2019-05-10 12:00'
appt.Subject = 'Ignore This Mail. It is a test mail'
appt.Duration = 30
appt.Location = 'CR-IND-BLR-PTP-FL4-Sundarbans-4L@wdc.com'
appt.MeetingStatus = 1 
appt.Recipients.Add("archan.mehta@wdc.com")
appt.Recipients.Add("PrakashVel.Periyannan@wdc.com")
appt.Save()
print ("Done")