import eliza


therapist = eliza.eliza()
while True:
  #get input from somewhere
  i = input()
  reply = therapist.respond(i)
  print(reply)