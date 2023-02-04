print("Welcome to The Mysterious Island.")
print("Your mission is to find the treasure and get out alive!\n\n") 

print("You wake up with the feeling of warm sand beneath you. You can feel the sun\nbeating down on your back, and gentle waves lap at your feet and legs. You\nopen your eyes and blink, raising your head to look around. You see you are on\na beach, and as you look around you can see the wreckage of a ship washed\nashore all around you. You remember then, the storm,the ship going down with\nyou still on board, the desperate swim for what looked like land, the flash of\nlightning and the waves, then black.\n")

print("You lick your lips as you lever yourself upright, trying to get your bearings.\nYou need water, and as you shade your eyes from the sun, you realize you need\nshade as well. Looking farther up the beach away from the sea, you can see a\ndense line of jungle and what looks like it might be a path leading deeper in.\n")

print("Looking back out to sea, you wonder if anyone is coming to rescue you. Should\nyou wait here and try to light a signal fire or head into the jungle and try\nto find water? You can’t forget either, you came here on a mission, find the\ntreasure!\n\n")

print("** What will you do? **\n")

go_stay = input("** Make a fire and try to wait for rescue or head into the jungle and try to\nfind water? **\n\n type 'fire' to stay or 'water' to go: \n=> ").lower()
if go_stay == str("fire"):
  print("\nYou decide to wait by the beach and see if anyone is coming. You look back\nat the forbidding line of jungle and though you are hot and thirsty, you\ndecide you can’t take the risk of going in there and getting lost. You start\nto gather up what you can for fire wood, ship wreckage, coconut husks,\nwhatever you can find. Once you have a nice big pile, you look for something\nyou can try to light the fire with. You see an old oil lamp has washed\nashore, with a little oil still at the bottom not fouled by sea water. You\ntake it and see not much farther up the beach is some flinty stone. Good\nthing you remember your old scouting lessons!\n\nYou take your finds back to your signal fire and manage to get it lit just\nas the sun is starting to set in the west. You wait and wait, but soon you\nrealize that no one is coming. As dawn is breaking, your fire long since\nburned to embers, you look back into the jungle behind you and know you are\non your own and will have to figure out a way to rescue yourself.\n")
  go_stay = input("** Make a fire and try to wait for rescue or head into the jungle and try to\nfind water? **\n\n type 'fire' to stay or 'water' to go: \n=> ").lower()
  if go_stay == str("fire"):
    print("You can't wait another day. You face the dawn a second time with no rescue in sight. Your throat is burning with thirst. You have to go in search of water or you'll die.\n")

if go_stay == str('water'):
  print("\n*You decide you can wait any longer, you need to try to find water. You head for the break in the foliage, hoping it might be a path and pleased when you see you\nwere right. As you push through the greenery, you see an old path through the\nundergrowth winding ahead of you. You can hear birds in the trees above you and\nas the leaves close behind you, you are enveloped by the warm moist air beneath\nthe canopy. It’s only marginally cooler than the beach, but at least the sun\nisn’t beating down on you anymore.\nYou think you can hear running water up ahead. As you walk, you see a small\nstream. You bend down and cup you hands in the cold water, washing your face and\nhands, and drinking as much as you can since you don’t know when the next time\nyou will find water is.") 
else:
  print("game reset")
 
print("Refreshed you stand up again, stepping over the small stream and follow the\npath father into the forest, until you come to a fork. You can turn left or right. Looking down both paths, they seem to be largely the same. You decide to take a chance.")

left_right = input("** Turn left or right? **\n\n type 'left' to take the left fork or 'right' to try the right path\n\n").lower()

if left_right == str("left"):
  print("* You decide to turn left * \nThe left hand fork looks just a little bit straighter, a little bit lighter. You decide to turn left, following along the path until you come to a small break in\nthe trees. As you come out into the sun, you see a flash of orange and hear a\nrumbling growl from the other side of the clearing. A tiger paces slowly out of\nthe gloom into the light, eyes locked on you. You freeze, unsure what to do next.\n\nYour monkey brain takes over, and you bolt! The tiger chases you, feet sure in\nthe braken of the forest floor. You stumble over a fallen log, no idea where the\npath has gotten to, just trying to get away. You hit your head as you fall,\nmercifully blacking out before you feel the tiger’s claws sink in.")

# print('')
 
# print("** You have died **")

# print('')
 
# print("* You decide to turn right *")

# print('')
 
# print("Despite the overgrown look of the right hand path, you to take the left hand\nfork. You continue up the path as it follows the stream, looping back and forth\nalong the bubbling little brook. You are beginning to fear that this isn’t a true\npath, and maybe just a game trail. You had hoped this might lead to some sort of\nvillage or town where you might be able to get some help. Now you aren’t so\nsure…")

# print('')
 
# print("As you continue along the path, though, you see lights ahead in the gloom of the\nforest. They are warm and look to be just out of easy shouting distance. The\nlights seem to be bobbing up and down gently, like someone carrying a torch.\nCould that be another person or people!?")

# print('')
 
# print("** Do you want to follow the lights or are you going to keep going the way you\nwere? **")

# print('')
 
# print("* Follow the lights into the forest *")

# print('')
 
# print("You can’t help it, the prospect of other people is too good to pass up. You leave the trail and try to follow the weaving bobbing lights. As you walk farther and\nfarther from the path, you call out to them hoping whoever they are will stop and\nwait for you. But they are always just a little to far. Finally, you stop,\nlooking around you and realize you are completely lost. You have no idea how to get back to the path or the beach now. As you look down, thinking to try to retrace your steps, you see that the ground here is suspiciously soft and muddy. As you watch, your footsteps fill with water and sink away out of sight. You look back along your own trail and see no trace of where you came from.")

# print('')
 
# print("As you stand, trying to think of something to do to get back to something you recognize you see the lights again. This time they are right in front of you. You reach out, calling out to them but they wink and float and you stand mesmerized watching their silent dance. Eventually you blink awake and try to take a step back. Its only then that you realize that you have sunk up to your waist in sticky mud, and you’re still sinking and fast.") 

# print('')
 
# print("The forest is silent around you as you sink below the surface, the mysterious lights still bobbing and weaving between the silent trunks of the great forest giants.")

# print('')
 
# print("** You have died **")

# print('')
 
# print("* Stay on the path *")

# print('')
 
# print("You pause and watch the lights for a time, but after being mesmerized by their dance, you blink awake and find that you have walked several paces off the path without realizing it. You quickly turn back, thinking to yourself that you don’t know what those lights are but you don’t like the look of them.") 

# print('')
 
# print("You see them a few more times as you walk along the trail, but each time they are just a little to far away. One time you could swear you hear singing or speaking as well, but just out of hearing range to be able to make out what they are saying. You shake your head and do your best to ignore it, vowing to stay on the path. Its got to go somewhere, right?")

# print('')
 
# print("** You come to a fork in the path. The right goes up, and you can see a break in the trees ahead. The left path goes down and curves away out of sight. What you can see of the path seems to be shrouded in a dense fog. **")

# print('')
 
# print("* You decide to turn right *")

# print('')
 
# print("You look at the two paths and decide that the left looks just a little too sketchy for your liking. You turn right, trudging up the steadily increasing incline. Soon you come to a break in the trees and you see that you are standing at the top of a cliff. Looking down, you can see trees and just beyond the beach where you washed ashore. Stepping forward, you shade your eyes hoping to be able to see a rescue ship in the distance. All you see is empty ocean to the horizon.") 

# print('')
 
# print("As you stand, straining your eyes for just a glimpse, you feel a rumble beneath you. As you stumble back, you feel the earth begin to slide from beneath your feet, and realize that the cliff is only loose soil! You tumble down, skating on the loose of the scree and finally fetch up hard against the trunk of a huge palm at the bottom. The wind is knocked from your chest, but after a bit you get your breath back and you drag yourself up right. Looking up, you see that you are now at the base of the cliff, almost back where you started this morning.")

# print('')
 
# print("Sighing and saying a few choice words, you trudge back to the beach to sit and nurse your scrapes. Its almost night, better to rest and decide in the morning what to do next. Gathering wood for a fire, you make a small camp and curl up beside it, hoping to get some sleep. Hopefully the dawn will bring better prospects that today…")

# print('')
 
# print("** Restart at the beach **")

# print('')
 
# print("* You follow the path to the left *")

# print('')
 
# print("It may look sketchy, but you reason that settlements are generally in valleys not on the top of hills, right? People build their houses by water, and water flows downhill not up. So, even though the fog is getting thick, and the sun is getting low on the horizon, you turn toward the left and head down into the valley.")

# print('')
 
# print("The fog on the ground is thick here, so thick that you have to be careful where you step because you can’t really see your feet. You try to stay with the path, which luckily has broadened here into something that almost looks like a real road. Sometimes, when there is a lifting of the fog, you see what almost looks like paving stones beneath your feet. They are broad and smooth, and have deep grooves worn down in places with greenery poking through cracks and breaks in other spots.")

# print('')
 
# print("Following the road, you come to what looks like a pair of standing stones on either side of the path. The great grey stones are covered in moss and lichen, and one leans precariously to the side. When you look closer, you can see deep groves cut in swirling patterns on the stones that seem to hum and emit an eerie light when you get close. The path leads between them, standing as silent guardians for whatever lies beyond.")

# print('')
 
# print("** Do you follow the path, or turn back? **")

# print('')
 
# print("* You decide to turn back *")

# print('')
 
# print("You retrace your steps back and find yourself back on the beach. Sighing and saying a few choice words, you see there are still no rescue ships in sight. Its almost night, better to rest and decide in the morning what to do next. Gathering wood for a fire, you make a small camp and curl up beside it, hoping to get some sleep. Hopefully the dawn will bring better prospects that today…")

# print('')
 
# print("** Restart at the beach **")

# print('')
 
# print("* You decide to be brave and explore the ruins *")

# print('')
 
# print("You run your fingers along the surface of the stone guardians, feeling a tingle like an electric current. Looking back the way you have come, you pause and almost turn back. But then you remember why you are here in the first place: The Treasure! You came all this way, it would be a shame not to see it through to the end, right?")

# print('')
 
# print("Walking between the guardian stones, for a moment the humming is so loud that you can’t hear anything else. You hold your hands over your ears, hoping to block out the strange sound. Abruptly, its gone and everything is silent. Not even the normal sounds of the jungle get through. All you can hear are your own echoing footsteps as you pace down the smooth paved stone of what is now clearly a street. There are ruined buildings on either side, stones tumbled around like building blocks, all covered in moss and lichen like the standing stones were.")

# print('')
 
# print("Following the lane, you finally come to a great stone building. Its seemingly the only thing still standing in the ruined square. It looms above you, imposing in its incongruity after all this time among the green of the jungle.")

# print('')
 
# print("You walk through arching entrance and as your eyes adjust to the dim interior, you see that in the center of the room is a stone pedestal, and on that pedestal is a set of golden balancing scales. On one side is what looks like a solid gold idol of some goddess, mouth open and screaming. On the other side is a single feather, emerald green in color and vibrant even in the gloom of the chamber.")

# print('')
 
# print("** Do you take the idol or the feather? **")

# print('')
 
# print("* You take the idol *")

# print('')
 
# print("The Treasure, at last! You look at the two scales and know right away which one you came here to get. You carefully take the idol, cringing and just waiting for something to pop out at you or fall or something… But nothing happens. The scale doesn’t tip, nothing moves. You smile to yourself, thinking thing are looking up at last!")

# print('')
 
# print("As you turn to go, there is the sound of stone scraping and you know you are about to have a deeply derivative moment as you look back over your shoulder. The scales are slowly tipping to the side with the feather, and the pedestal is starting to crumble. Cracks travel quickly outward, crazing up the walls as dust is kicked up by the shaking. You realize its not just the building as you run outside and see the whole village is shaking, building tumbling down even more than they already had. You run, the golden idol clutched to your chest and the earth shakes in your wake.")

# print('')
 
# print("It seems like you race the earthquake all the way back to the beach, and as you stumble onto the sands just as the sun sets you can see the ocean retreating and a monstrous wave climbs up the horizon. You clutch your prize, and are helpless to stop it as the sea comes to claim you, dragging and the idol along in its wake. You lose hold of it and the last thing you feel before you run out of breath is the earth subsiding around you as if with this one great upheaval, some great beast has been appeased.")

# print('')
 
# print("* You take the feather *")

# print('')
 
# print("You look at the idol and as your hand reaches forward, some intuition stays your hand. You remember all too well how that ended in every tale of adventure you have ever heard. The hero who takes the golden idol never ends well.")

# print('')
 
# print("Looking at the other side of the scale, you examine the feather. It glints bright in the gloom, almost with a light of its own. The green blue hues ripple over its surface such that you can’t entirely tell if its a real feather or something crafted of the finest gems. Entranced, you extend you hand out and brush you fingers along the length of the feather. Its surprisingly soft to the touch, and you find yourself picking it up carefully by the shaft.")

# print('')
 
# print("Holding the feather up a shaft of light coming through a crack in the roof, you see hints of peacock blue and a dusting of gold play along the surface. As you hold it aloft, you feel a monstrous pain sieze your whole body. You convulse, clutching the feather to yourself as you collapse to your knees in the dust of the cavernous room.")

# print('')
 
# print("As your eyes begin to blur from the pain, you look up and see the paintings on the walls of the room that you had failed to notice before. They seem to portray men with the faces of bird, with wings spread wide. As another cramp curls you in on yourself, you feel something push its way under your skin and then push through. Slowly, tears streaming down your face, you feel as the wings grow from your back until finally you stand in unconscious imitation of the hieroglyphs on the wall, emerald green wings spread wide. Walking out of the building, you see you are not alone. Other winged men and women are there, faces shrouded in masks of birds and foxes and deer.")

# print('')
 
# print("One man spreads his golden hawk wings wide, holding out an emerald green mask to you. You see your hands reaching out to it, feel yourself taking the mask and donning it, and you finally know that you are where you are meant to be.")

