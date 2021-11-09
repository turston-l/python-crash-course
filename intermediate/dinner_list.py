guests = ['wallace wattles', 'bob proctor', 'steve pavlina']
invitation_1 = f'{guests[0].title()}, I would like to invite you to dinner.'
invitation_2 = f'{guests[1].title()}, I would like to invite you to dinner.'
invitation_3 = f'{guests[2].title()}, I would like to invite you to dinner.'
print(invitation_1)
print(invitation_2)
print(invitation_3)
print(f"Unfortunately, {guests[0].title()} won't be able to make it.")
removed_guest = guests.pop(0)
guests.insert(0, 'david icke')
print(removed_guest.title())
print(invitation_1)
print(invitation_2)
print(invitation_3)
print(guests)
print(invitation_1)
print(invitation_2)
print(invitation_3)

invitation_1 = f'{guests[0].title()}, I would like to invite you to dinner.'
invitation_2 = f'{guests[1].title()}, I would like to invite you to dinner.'
invitation_3 = f'{guests[2].title()}, I would like to invite you to dinner.'
print(invitation_1)
print(invitation_2)
print(invitation_3)

print("We've found a bigger dinner table.")

guests.insert(0, 'jordan peterson')
guests.insert(2, 'james clear')
guests.append('val de vall')

invitation_1 = f'{guests[0].title()}, I would like to invite you to dinner.'
invitation_2 = f'{guests[1].title()}, I would like to invite you to dinner.'
invitation_3 = f'{guests[2].title()}, I would like to invite you to dinner.'
invitation_4 = f'{guests[3].title()}, I would like to invite you to dinner.'
invitation_5 = f'{guests[4].title()}, I would like to invite you to dinner.'
invitation_6 = f'{guests[5].title()}, I would like to invite you to dinner.'
print(invitation_1)
print(invitation_2)
print(invitation_3)
print(invitation_4)
print(invitation_6)


print("We can invite only two people for dinner.")

popped_1 = guests.pop()
print(f'Sorry {popped_1.title()}, I can no longer invite you.')
popped_2 = guests.pop()
print(f'Sorry {popped_2.title()}, I can no longer invite you.')
popped_3 = guests.pop()
print(f'Sorry {popped_3.title()}, I can no longer invite you.')
popped_4 = guests.pop()
print(f'Sorry {popped_4.title()}, I can no longer invite you.')

print(f'You are still invited {guests[0].title()}')
print(f'You are still invited {guests[1].title()}')


print(guests)