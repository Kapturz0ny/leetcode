class Solution:
	def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
		if len(sentence1) > len(sentence2):
			main_s = sentence2.split(" ")
			sup_s = sentence1.split(" ")
		else:
			main_s = sentence1.split(" ")
			sup_s = sentence2.split(" ")

		i, j = 0, 0
		insert_spot_found = False
		second_spot_req	= False
		finish = False
		snd_chance_keep_inserting = False
		while j < len(sup_s):
			print(main_s[i], sup_s[j])
			if main_s[i] == sup_s[j]:
				j += 1
				if i < len(main_s) - 1:
					i += 1
				else: 
					finish = True
				if insert_spot_found:
					second_spot_req = True
			else:
				if second_spot_req:
					if snd_chance_keep_inserting:
						return False
				else:
					j += 1
					insert_spot_found = True
			print(insert_spot_found, second_spot_req)

		if finish:
			return True
		else:
			return False