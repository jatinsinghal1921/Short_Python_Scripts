import win32com.client


outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")


def get_inboxFolder_data():
    inbox = outlook.GetDefaultFolder(6) # "6" refers to the index of a folder - in this case,
                                        # the inbox. You can change that number to reference
                                        # any other folder
    messages = inbox.Items
    print("Total Number of Messages in Inbox Folder: " + str(len(messages)))
    
    # Sorting the messages in Descending Order based on Received Time. The one which is received recently will be at 0th position. 
    messages.Sort("[ReceivedTime]", False)

    # Fetching the Contents of Latest Message in Inbox Folder
    last_msg = messages.GetLast()
    last_msg_sender_email = last_msg.SenderEmailAddress
    last_msg_sender_name = last_msg.SenderName
    last_msg_subject = last_msg.Subject
    last_msg_body_content = last_msg.body
    last_msg_class = last_msg.Class
    # print ("Sender Name of the Last Message : " + str(last_msg_sender_name))
    # print ("Sender Email of the Last Message : " + str(last_msg_sender_email))
    # print("Subject of the Last Message : " + str(last_msg_subject))
    # print("Class of the Last Message : " + str(last_msg_class))
    # print("Content in Last Message : \n" + str(last_msg_body_content))
    # if last_msg.Unread == True:
    #     print("Latest message is still not read")
    # else:
    #     print("Latest message is already read by you.")


    # Traversing the messages list which are from Pallab, contain 'Release' Keyword in Subject and are of class 43. 
    for index in range(len(messages)):
        message = messages[len(messages)-1-index]
        if "release" in str(message.Subject).lower() and "pallab" in str(message.SenderName).lower() and message.Class == 43:
            # print(message.Subject)
            if "a0020q3n" in str(message.Subject).lower():
                lines = str(message.body).split("\n")
                for line in lines:
                    # print(line)
                    if "\\ipa_develop_reduced_cap\\_out.7z" in line:
                        print(line)


    return inbox


def subfolders_in_inbox(inbox):
    for subfldr in inbox.Folders:
        print(subfldr)


def main():
    print("************ Printing Inbox Folder Data ******************")
    inbox = get_inboxFolder_data()


if __name__ == "__main__":
    main()