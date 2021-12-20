import os

import pykintone

from src.model.Hankyo import Hankyo
from src.helper.slack import sendToSlackFormatted
from src.helper.args import getArgByIdx

#Environment variable loader
from dotenv import load_dotenv
load_dotenv()

#Initialize App
import pathlib
currentPath = pathlib.Path(__file__).parent.resolve()
print("current", currentPath)
account = pykintone.load(os.path.join(currentPath, "account.yml"))
app = account.app()

def registerToKintone(title, main, mailTo, mailFrom):
  try:
    print("Trying to register.")
    record = Hankyo()
    record.title = title
    record.main = main
    record.mail_to = mailTo
    record.mail_from  = mailFrom
    result = app.create(record)
    return result.record_id
  except:
    print("Failed")



def main():

  # ArgsIdx
  # 1 = title
  # 2 = main
  # 3 = mailTo
  # 4 = mailFrom

  _title = getArgByIdx(1)
  _mailTo = getArgByIdx(3)

  _recordId = registerToKintone(title=_title, main=getArgByIdx(2), mailTo=_mailTo, mailFrom=getArgByIdx(4))

  sendToSlackFormatted(_recordId, _title, _mailTo)

if __name__ == "__main__":
  main()