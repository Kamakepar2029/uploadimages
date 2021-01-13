import requests as ph

def get1(number):
  try:
      number = number.replace("+7","")
      number = number.replace("+360","")
      number = number.replace("+380","")
      number = number.replace("+39","")
      number = number.replace("+40","")
      number = number.replace("+38","")
      number = number.replace("+36","")
      number = number.replace("+35","")
      number = number.replace("+31","")
      number = number.replace("+30","")
      number = number.replace("+29","")
      number = number.replace("+28","")
      number = number.replace("+27","")
      number = number.replace("+26","")
      number = number.replace("+25","")
      number = number.replace("+24","")
      number = number.replace("+23","")
      number = number.replace("+22","")
      number = number.replace("+21","")
      number = number.replace("+20","")
      number = number.replace("+19","")
      number = number.replace("+18","")
      number = number.replace("+17","")
      number = number.replace("+16","")
      number = number.replace("+15","")
      number = number.replace("+14","")
      number = number.replace("+13","")
      number = number.replace("+12","")
      number = number.replace("+11","")
      number = number.replace("+10","")
      number = number.replace("+9","")
      number = number.replace("+8","")
      number = number.replace("+7","")
      number = number.replace("+6","")
      number = number.replace("+5","")
      number = number.replace("+4","")
      number = number.replace("+3","")
      number = number.replace("+2","")
      number = number.replace("+1","")
      url = "https://phoneregion.ru/number/"+str(number)
      sol = ph.get(url)
      mass = ((sol.text).replace("<br>","")).split('<div id="result">')
      massive = mass[1].split('</div>')
      #print(massive[0])
      #print(massive[0])
      #print("_____________________________")
      #sopl = (massive[0].replace("\n",""))
      #sopl = sopl.replace("  ","")
      #sopls = sopl.split('<br />')
      #print('________________________________')
      reion = massive[0].split('<span class="region">')
      region = reion[1].split('</span>')
      operat = region[1].split('<span class="operator">')
      opertor = operat[1].split('</span>')
      operator = opertor[0]
      soplo = region[0]
      #print(operator)
      #print(soplo)
      #print('________________________________')
      allapp = '🏦  '+soplo+'\n'+'🧩  '+operator
      return (allapp)
      pass
  except:
      return ('⛔️ No thing found or some error!')
      pass 
def get_record(number):
   try:
      number = number.replace("+7","")
      number = number.replace("+360","")
      number = number.replace("+380","")
      number = number.replace("+39","")
      number = number.replace("+40","")
      number = number.replace("+38","")
      number = number.replace("+36","")
      number = number.replace("+35","")
      number = number.replace("+31","")
      number = number.replace("+30","")
      number = number.replace("+29","")
      number = number.replace("+28","")
      number = number.replace("+27","")
      number = number.replace("+26","")
      number = number.replace("+25","")
      url = "https://xn--90aakbpnp1abtmc.xn--p1ai/phone/"+str(number)
      sol = ph.get(url)
      if ('<div class="post-box__content" itemprop="description">' in sol.text):
         return '⚠️ Something is said about this number in the spam base.\nGet to the url: '+url
      else:
         return ('❌ Nothing about this number in the spam base')
         pass
   except:
      return '⛔️ Something went wrong'
      pass


print(get1('+79636487248'))
