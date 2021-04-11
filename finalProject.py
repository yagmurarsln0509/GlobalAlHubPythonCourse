class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer
question_prompts = [ 
             "Türkiye'nin başkenti neresidir ? " , 
            "Türkiye'nin ilk cumhurbaşkanı kimdir ? "  ,
            "Hangi gezegende yaşıyoruz ? ",
            "Dünya'nın en büyük okyanusu nedir ? ",
             "Suyun kimyasal förmülü nedir ? " ,
             "Amerika Birleşik Devletlerinin ilk başkanın adı nedir ? "  , 
             "Yerden fışkırarak çıkan su kaynaklarına ne denir? " ,
             "Depremin büyüklüğünü ölçen alet nedir ? ",
             "Türkiye'nin en kalabalık şehiri nedir ? "  ,
             "Ses en hızlı hangi ortamda yayılır? " ,
            ] 
questions = [
     Question(question_prompts[0], "Ankara" ),
     Question(question_prompts[1], "Atatürk"),
     Question(question_prompts[2], "Dünya"),
     Question(question_prompts[3], "Pasifik"),
     Question(question_prompts[4], "H2o"),
     Question(question_prompts[5], "Benjamin"),
     Question(question_prompts[6], "Gayzer"),
     Question(question_prompts[7], "Sismograf"),
     Question(question_prompts[8], "İstanbul"),
     Question(question_prompts[9], "Katı")
              
              ]

def run_quiz(questions):
     score = 0
     for question in questions:
         print("\n Lütfen baş harfleri büyük yazınız")
         answer = input(question.prompt)
         if answer == question.answer:
               score += 10
     print("\n Puanınız {0}/100.".format(score))
     
     if score > 50 :
      print("Tebrikler! Sınavı başarı ile geçtiniz.")
     else:
      print("Sınavı geçemediniz...")

run_quiz(questions) 