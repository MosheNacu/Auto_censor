import speech_recognition as sr
import msvcrt

r = sr.Recognizer()

profanities = ['shit', 'fuck', 'fucker', 'motherfucker', 'slut', 'nigger', 'whore', 'asshole', 'dick', 'shrek']

with sr.Microphone() as source:
	while True:
		print("Speak Anything :")
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
		try:
			text = r.recognize_google(audio)
			print(">>> ",text)
			if text == "exit":
				print("Exiting")
				break

			#parse by word
			words = text.split()
			#censors profanities
			for w in words:
				if w in profanities:
					i = words.index(w)
					censored = w
					censored = censored[0] + ("*" * (len(w)-1))
					words[i] = str(censored)

			print(words)
		except:
			print("Sorry could not recognize what you said")