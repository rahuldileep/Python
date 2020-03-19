class solution():
	def change_domain(self, email, old_domain, new_domain):
		if '@'+old_domain in email:
			local_index = email.index('@'+old_domain)
			domain_index = email.index('.',local_index)
			email = email[:local_index] + '@' + new_domain +email[domain_index:]
		return email
		
object = solution()
print(object.change_domain('reesha@hotmail.com','hotmail','gmail'))