

#1 ... Hello World up and running. Sill  stick figure moves across the screen. 
#2 ... simple collision + start animation of stick figure and fence. 
#3 ---> FRIDAY: Make the animation walk nicely across the screen. 





TODO
=======
1. Design Game Entities: Sketch out how the defender (house), attacker and electric line should look.
2. Set up the Game Board: Set up the visual aspects of the game board like background, lines etc.
3. Create Defender: Implement graphical representation of the house. As it is static, not much functionality needs to be associated with it.
4. Create Attacker: Implement the attacker entity. Initially, it can be stationary.
5. Implement Attacker Movement: Make the attacker move towards the defender.
6. Create Electric Line: Implement the electric line representing the fence.
7. Keyboard Interaction: Connect keyboard, particularly space button, so that pressing it electrifies the fence.
8. Fence Animation: Create an animation or visual effect for when the fence is electrified.
9. Implement Collision Detection: While the fence is electrified, if the attacker comes in contact, then trigger a certain response (like ending game, reducing attacker's health etc).
10.Attacker Electrification Animation: Have a different animation for when the attacker is electrified.
11. Defender Loss Animation: Have a different animation for when the house is lost/attacked.
12.  Implement Sound Effects: Add sound effects for various events as specified.
a) Attacker coming
b) Electric fence active
c) Attacker being electrified
d) House is lost.

13. Test: Test the game thoroughly to make sure all components are working together.
14. Refine: Based on testing, refine the graphics, motion, sound effects.
15. Release: After all stages have been tested and refined, you can release your game.





GOAL --- MVP
1. A figure moves from left to right. 
2. There's an electric line on the right side of the screen. Behind the line is a defender. 
3. If the defender. hits the electric-on button, then the fence will be electrified for 1 second. 
4. If the attacker touches the electrified line, the attacker will be electrocuted for 1 second die. 
5. If the attacker walks past the line, without being electrified, then the defener will loose. 
