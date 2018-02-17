import scraper
import schemata
import random


def filter_f(x):
  if len(x)<5:
    return False
  else:
    return x[-5:] == "_joke"



def handle_reqs(schemata_req,driver):
  results = [None,None,None,None]
  for req in schemata_req[:-1]:
    if req[:3] == "hom":
      a = req.split()[1:]
      nounity1 = schemata_req[-1].split()[int(a[0])-1]
      nounity2 = schemata_req[-1].split()[int(a[1])-1]
      b,_,c,_ = driver.get_specific_random_homophones(nounity1,nounity2)
      results[int(a[0])-1] = b
      results[int(a[1])-1] = c
    if req[:3] == "syn":
      a = req.split()[1:]
      if results[int(a[0])-1] != None:
        syno = driver.get_synonym(results[int(a[0])-1])
        results[int(a[1])-1] = syno
      elif results[int(a[1])-1] != None:
        syno = driver.get_synonym(results[int(a[1])-1])
        results[int(a[1])-1] = syno
      else:
        raise ValueError
  return results
          
      
  

driver = scraper.Driver()
schemata_names = filter(filter_f,dir(schemata))
# schemata_name = schemata_names[random.randint(0,len(schemata_names))]
schemata_name = "N2A2_joke"
schemata_f = getattr(schemata, schemata_name)
schemata_req = getattr(schemata, schemata_name[:-5]+"_req")
[d1,d2,w1,w2] = handle_reqs(schemata_req(),driver)
schemata(d1,d2,w1,w2)
   
