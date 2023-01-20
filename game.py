from tkinter import *
import random
import time
#import pygame

root = Tk()
root.title("BRUH")
root.geometry('500x400+200+100')
a_button = Button(text = 'Start', width=40,height=5)
b_button = Button(text = 'Exit', width=40,height=5)
def Exit(event):
   global root
   root.destroy()
   sys.exit()
   



characters = ('medic', 'enginer', 'belligerence', 'intellect',
              'charisma', 'perception', 'guide')
emp = ('Galactic Empire','Free Planets Alliance')
tt = ('Рядовой', 'Ефрейтор', 'Капрал', 'Сержант', 'Старший сержант',
      'Старшина','Мичман','Младший лейтенант','Лейтенант','Старший лейтенант',
      'Капитан 3-го ранга','Капитан 2-го ранга','Капитан 1-го ранга','Коммодор',
      'Контр-адмирал','Вице-адмирал','Адмирал','Адмирал флота','Гранд-адмирал')
lvl = ((0,0), (1,3), (2,3), (3,5), (4,5), (5,7), (6,7), (7,10),
       (8,7), (9,5), (10,3), (11,1), (12,1), (13,1), (14,1),
       (15,1), (16,1), (17,1), (18,1), (19,1))
template_name_male = ('Борислав', 'Игнат', 'Харитон', 'Макар', 'Потап',
                 'Анастасий', 'Пахом', 'Федот', 'Донат', 'Алмаз',
                 'Мухтар', 'Юнус',)
template_name_female = ('Ия', 'Платонида', 'Искра', 'Фекла',
                 'Цецилия', 'Одетта', 'Нурия', 'Илюза')
type_ship = ('Battleship', 'Flagship', 'Carrier', 'Cruiser',
             'Destroyer', 'Strike ship', 'Transport')
SHIPS = {'Free Planets Alliance':
                           ({'Battleship':
                                              ({'Gumeiya': {'name': 'Gumeiya',
                                                'health': 100, 'damage': 10, 'need_lvl': 1,
                                                'critical damage': 20, 'energy': 60}},
                                               {'Ulysses': {'name': 'Ulysses',
                                                'health': 150, 'damage': 20, 'need_lvl': 2,
                                                'critical damage': 35,  'energy': 70}},
                                               {'Hyperion': {'name': 'Hyperion',
                                                'health': 200, 'damage': 30, 'need_lvl': 0,
                                                'critical damage': 50, 'energy': 100}})},

                            {'Flagship':( {'Ajax': ({'name': 'Ajax',
                                                'health': 200, 'damage': 30, 'need_lvl': 1,
                                                'critical damage': 50, 'energy': 100})})},
                            {'Carrier':
                                         {'Alliance carrier (788 UC era)': {'name': 'Alliance carrier (788 UC era)',
                                                                            'need_lvl': 1}}},
                            {'Cruiser':
                                         {'Alliance cruiser (745 UC era)': {'name': 'Alliance cruiser (745 UC era)',
                                                                            'need_lvl': 1}}},
                            {'Destroyer':
                                         {'Alliance destroyer (745 UC era)': {'name': 'Alliance destroyer (745 UC era)',
                                                                            'need_lvl': 1}}},
                            {'Strike ship':
                                         {'Alliance strike ship (788 UC era)': {'name': 'Alliance strike ship (788 UC era)',
                                                                            'need_lvl': 1}}},
                            {'Transport':
                                         {'Alliance transport (788 UC era)': {'name': 'Alliance transport (788 UC era)',
                                                                            'need_lvl': 1}}}),
         'Galactic Empire':
                           ({'Battleship':
                                              ({'Asgrimm': {'name': 'Asgrimm',
                                                'health': 100, 'damage': 10, 'need_lvl': 0,
                                                'critical damage': 20, 'energy': 60}},
                                               {'Audhumla': {'name': 'Audhumla',
                                                'health': 150, 'damage': 20, 'need_lvl': 1,
                                                'critical damage': 35,  'energy': 70}},
                                               {'Berlin': {'name': 'Berlin',
                                                'health': 200, 'damage': 30, 'need_lvl': 0,
                                                'critical damage': 50, 'energy': 100}})},

                            {'Flagship':( {'Ajax': ({'name': 'Ajax',
                                                'health': 200, 'damage': 30, 'need_lvl': 1,
                                                'critical damage': 50, 'energy': 100})})},
                            {'Carrier':
                                         {'Hässliche Entlein': {'name': 'Hässliche Entlein',
                                                                            'need_lvl': 1}}},
                            {'Cruiser':
                                         {'Bremen': {'name': 'Bremen',
                                                                            'need_lvl': 1}}},
                            {'Destroyer':
                                         {'Hameln II': {'name': 'Hameln II',
                                                                            'need_lvl': 1}}},
                            {'Strike ship':
                                         {'Imperial strike ship (788 UC era)': {'name': 'Imperial strike ship (788 UC era)',
                                                                            'need_lvl': 1}}},
                            {'Transport':
                                         {'Imperial transport (788 UC era)': {'name': 'Imperial transport (788 UC era)',
                                                                            'need_lvl': 1}}})}
                      
         
class P:
   def __init__(self, name, empire, clas = 'нет', title = tt[0], score = 0):
      self.name = name
      self.empire = empire
      self.clas = clas
      self.title = title
      self.level = 0
      self.sc = score
      self.ship = 0
      self.gender = []
      
   def stats(self, medic=1, enginer=1, belligerence=1, intellect=1,
             charisma=1, perception=1, guide=1):
      self.medic = medic
      self.enginer = enginer
      self.belligerence = belligerence
      self.intellect = intellect
      self.charisma = charisma
      self.perception = perception
      self.guide = guide
      
   
   def lvl_up(self):
      global j, level
      j=self.__dict__[characters[self.level]]
      def lvl_pups(event):
         global j
         j-=1
         char = event.widget.cget('text')
         char_formated = ''
         for i in char:
            if i == ' ':
               break
            char_formated += i
         
            
         self.__dict__[char_formated]+=1
         print(char_formated, self.__dict__[char_formated])
         dud = char_formated + ' - ' + str(self.__dict__[char_formated])
         event.widget.config(text=dud)
         self.sc -= 1
         huh = 'Что хотите улучшить?. Очков осталось - ' + str(self.sc)
         print(huh)
         l1.config(text = huh)
         l1.update()
         if self.sc == 0:
            a.destroy()
      
      a = Toplevel()
      self.level += 1
      self.sc = lvl[self.level][1]
      ss = self.sc
      print(ss)
      xyx = 'Что хотите улучшить?. Очков осталось - ' + str(self.sc)
      l1 = Label(a,text=xyx, font="Arial 20")
      
      chuch = ''
      buttons = []
      l1.pack()
      
      for i in range(len(characters)):
         chuch = str(characters[i]) + ' - ' + str(self.__dict__[characters[i]])
         buttons.append(Button(a,text=chuch, width=40,height=5))
         buttons[-1].bind('<Button-1>', lvl_pups)
         print(self.__dict__[characters[i]])
         buttons[-1].pack()
         
     #так ты да же а но не не гей?
     #кто умрет тот прочитал
      
      
   def vibori(self):
      global ship_e, l1, e1, a_button, b_button, c_button, d_button, e_button, buttons, a, v_button
      if gender == 'female':
         def Exit(event):
            global root, lal, f_button
            root.destroy()
            sys.exit()
         l1.destroy()
         e1.destroy()
         a_button.destroy()
         b_button.destroy()
         c_button.destroy()
         d_button.destroy()
         e_button.destroy()
         l1 = Label(text='Женщине не место на корабле!', font="Arial 20")
         a_button = Button(text='ЯСНА ПАНЯТНА', width=40,height=5)
         a_button.bind('<Button-1>', Exit)
         l1.pack()
         a_button.pack()
         
      else:
         global a, v_button
         a = Toplevel()
         a.geometry('500x500+200+100')
         lal = Label(a,text='Какой тип?', font="Arial 20")
         f_button = Button(a,text='Battleship', width=40,height=5)
         buttons = []
         cac = []
         def Exit(event):
            global root, lal, f_button
            a.destroy()
            sys.exit()
         v_button = Button(a,text='Exit', width=40,height=5)
         v_button.bind('<Button-1>', Exit)
         
         def sheep(event):
            global v_button, type_ship
            v_button.destroy()
            def karablik(event):
               global type_ship, ship
               self.ship = []
               cac = eval(event.widget.cget('text'))
               coc = cac['name']
               self.ship.append(coc)
               ship = Ship(cac['name'], type_ship, cac['health'], cac['damage'],
                           cac['critical damage'], cac['energy'])
               a.destroy()
            for i in SHIPS[self.empire]:
                     for z in i:
                           type_ship = z
                           for r in i[z]:
                                 for q in r:
                                       try:
                                             if r[q]['need_lvl'] <= self.level:
                                                   lal.destroy()
                                                   f_button.destroy()
                                                   
                                                   aya = r[q]
                                                   jj=[0]
                                                   jj.append(r[q]['name'])
                                                   buttons.append(Button(a,text=aya))
                                                   buttons[-1].bind('<Button-1>', karablik)
                                                   buttons[-1].pack()
                                                   
                                                   
                                                   
                                             else:
                                                Button(a, text='ERRORRR... Требуется звание выше.').pack()
                                             
                                       except:
                                             continue

            
         f_button.bind('<Button-1>', sheep)
         lal.pack()
         f_button.pack()
         v_button.pack()
         


class Ship():
   def __init__(self, name, type_ship, health, damage, critical_damage, energy, level=0):
      self.name = name
      self.type = type_ship
      self.hp = health
      self.dmg = damage
      self.level = level
      self.crit = critical_damage
      self.st = energy
   def Attack(self, vrag):
      global l1, e1, a_button, b_button, c_button, d_button, e_button, l_p, l_pers_ship
      en = self.st
      if ship.hp <= 0:
         l1.destroy()
         e1.destroy()
         l_p.destroy()
         l_pers_ship.destroy()
         a_button.destroy()
         b_button.destroy()
         c_button.destroy()
         d_button.destroy()
         e_button.destroy()
         def Exit(event):
            global root
            root.destroy()
            sys.exit()
         a_button = Button(text = 'GAME OVER', width=40,height=5)
         a_button.bind('<Button-1>', Exit)
         a_button.pack()
            
         #j = random.randint(0,1)
      if self.st <= 0:
         self.st = en
         pop = 'Имя корабля:' + self.name + ' ' + 'Жизнь:' + str(self.hp) + ' ' + 'Атака:' + str(self.dmg) + ' ' + 'Энергия' + str(self.st)
         #l_p.config(text = pop)
         #l_p.update()
      else:
         self.st -= 10
         vrag.hp -= self.dmg
         pap = 'Имя корабля:' + vrag.name + ' ' + 'Жизнь:' + str(vrag.hp) + ' ' + 'Атака:' + str(vrag.dmg) + ' ' + 'Энергия' + str(vrag.st)
         l_pers_ship.config(text = pap)
         l_pers_ship.update()
         pop = 'Имя корабля:' + self.name + ' ' + 'Жизнь:' + str(self.hp) + ' ' + 'Атака:' + str(self.dmg) + ' ' + 'Энергия' + str(self.st)
         l_p.config(text = pop)
         l_p.update()

   
            
def Start(event):
   global a_button, b_button, l1, ship_e
   a_button.destroy()
   b_button.destroy()
   ship_e = []
   l1 = Label(text="Выберите державу.", font="Arial 20")
   a_button = Button(text = 'Galactic Empire', width=40,height=5)
   b_button = Button(text = 'Free Planets Alliance', width=40,height=5)
   a_button.bind('<Button-1>', Empire)
   b_button.bind('<Button-1>', Empire)
   l1.pack()
   a_button.pack()
   b_button.pack()

def Empire(event):
   global emp, a_button, b_button, c_button, l1, gender, empire, a
   emp = event.widget.cget('text')
   pers.empire = emp
   l1.destroy()
   a_button.destroy()
   b_button.destroy()
   l1 = Label(text="Выберите пол.", font="Arial 20")
   b_button = Button(text = 'male', width=40,height=5)
   a_button = Button(text = 'female', width=40,height=5)
   c_button = Button(text = 'futanari', width=40,height=5)
   
   def femka(event):#не смешно
      global gender
      gender = 'female'
      print(gender)
      Name()
   def man(event):
      global gender
      gender = 'male'
      print(gender)
      Name()
   def shemale(event):
      global gender
      gender = 'it'
      print(gender)
      Name()
   a_button.bind('<Button-1>', femka)
   b_button.bind('<Button-1>', man)
   c_button.bind('<Button-1>', shemale)
   l1.pack()
   a_button.pack()
   b_button.pack()
   c_button.pack()
   
def Name():
   global a_button, b_button, c_button, l1, e1, gender, name, a
   l1.destroy()
   a_button.destroy()
   b_button.destroy()
   c_button.destroy()
   l1 = Label(text="Выберите имя.", font="Arial 20")
   e1 = Entry(width=50)
   a_button = Button(text = 'Автовыбор', width=40,height=5)
   b_button = Button(text = 'ОК', width=40,height=5)
   def At_name(event):
      global name, a
      if gender == 'male':
         ll = len(template_name_male)
         rr = random.randrange(0, ll)
         name = template_name_male[rr]
         print(name)
      elif gender == 'it':
         lol = template_name_male + template_name_female
         ll = len(template_name_male) + len(template_name_female)
         rr = random.randrange(0, ll)
         name = lol[rr]
         print(name)
      else:
         ll = len(template_name_female)
         rr = random.randrange(0, ll)
         name = template_name_female[rr]
         print(name)
      pers.name = name
      e1.delete(0, END)
      e1.insert(0,name)
   def OK(event):
      global name
      name = e1.get()
      print(name)
      Menu()
   a_button.bind('<Button-1>', At_name)
   b_button.bind('<Button-1>', OK)
   l1.pack()
   e1.pack()
   a_button.pack()
   b_button.pack()
def Menu():
   global l1, e1, a_button, b_button,c_button, d_button, pers, a, e_button
   pers.stats()
   l1.destroy()
   e1.destroy()
   a_button.destroy()
   b_button.destroy()
   l1 = Label(text="Что хотите сделать?", font="Arial 20")
   a_button = Button(text = 'Вывести общую информацию.', width=40,height=5)
   b_button = Button(text = 'BOOM!', width=40,height=5)
   #c_button = Button(text = 'лвл упс', width=40,height=5, command = pers.lvl_up)
   d_button = Button(text = 'выборы кораблей 2707', width=40,height=5, command = pers.vibori)
   e_button = Button(text = 'Пойти в космос', width=40,height=5)
   def Exit(event):
      global root
      root.destroy()
      sys.exit()
   a_button.bind('<Button-1>', Infa)
   b_button.bind('<Button-1>', Exit)
   e_button.bind('<Button-1>', Battle)
   l1.pack()
   a_button.pack()
   b_button.pack()
   #c_button.pack()
   d_button.pack()
   e_button.pack()
   
def Battle(event):
   global l1, e1, a_button, b_button, c_button, d_button, e_button, l_p, l_pers_ship
   l1.destroy()
   e1.destroy()
   a_button.destroy()
   b_button.destroy()
   c_button.destroy()
   d_button.destroy()
   e_button.destroy()
   if pers.ship == 0:
      l1 = Label(text='Отсутствует корабль.', font="Arial 20")
      a_button = Button(text = 'OK.', width=40,height=5)
      def back(event):
         Menu()
      a_button.bind('<Button-1>', back)
      l1.pack()
      a_button.pack()
   else:
      l1 = Label(text='На вас нападают космические пираты.', font="Arial 20")
      helth_p = random.randrange(50,200,10)
      damage_p = random.randrange(0,50,5)
      energy_p = random.randrange(20,100,20)
      pirate = Ship('Pirate', 'Battleship', helth_p, damage_p, 1000, energy_p)
      pop = 'Имя противника:' + pirate.name + ' ' + 'Жизнь:' + str(pirate.hp) + ' ' + 'Атака:' + str(pirate.dmg) + ' ' + 'Энергия' + str(pirate.st)
      pap = 'Имя вашего корабля:' + ship.name + ' ' + 'Жизнь:' + str(ship.hp) + ' ' + 'Атака:' + str(ship.dmg) + ' ' + 'Энергия' + str(ship.st)
      l_p = Label(text=pop, font="Arial 10")
      l_pers_ship = Label(text=pap, font="Arial 10")
      def qeq(evevnt):
         j = random.randint(0,1)
         if j == 0:
            pirate.Attack(ship)
         else:
            ship.Attack(pirate)
      a_button = Button(text = 'tatakae', width=40,height=5)
      a_button.bind('<Button-1>', qeq)
      
      
      l1.pack()
      l_p.pack()
      l_pers_ship.pack()
      a_button.pack()
      
      
def Infa(event):
   global l1, e1, a_button, b_button, c_button, d_button, e_button, gender, name, empire, ship_e, pers
   l1.destroy()
   e1.destroy()
   a_button.destroy()
   b_button.destroy()
   c_button.destroy()
   d_button.destroy()
   e_button.destroy()
   print(pers.name, pers.empire, pers.clas, pers.title, str(pers.level), str(pers.ship))
   if ship_e == []:
      ship_e = 'нет'
   fof = 'Имя: ' + pers.name + '\nДержава: ' + pers.empire + '\nСпециализация: ' + pers.clas + '\nЗвание: ' + pers.title + '\nУровень ' + str(pers.level) +'\nkarabl ' + str(pers.ship)
   l1 = Label(text=fof, font="Arial 20")
   def back(event):
      Menu()
   a_button = Button(text = 'Назад.', width=40,height=5)
   a_button.bind('<Button-1>', back)
   l1.pack()
   a_button.pack()
name = ''
empire = ''
gender = ''
pers = P(name, empire)
pers.gender = gender

a_button.bind('<Button-1>', Start)
b_button.bind('<Button-1>', Exit)
a_button.pack()
b_button.pack()
root.mainloop()
