from tika import parser

raw = parser.from_file('C:\\Users\\39231\\Desktop\\NVMe - PCIe\\NVM_Express_Revision_1.3.pdf')
pdf_data = raw['content'].strip().encode("utf-8")
pdf_data_file = open("pdf_data.txt","wb")
pdf_data_file.write(pdf_data)