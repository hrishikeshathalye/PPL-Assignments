:- initialization(main).
main :- write('\n\nWelcome to the flight management system').

/*Below are the facts regarding airports*/
/*airport(city, airporttax, minsecuritydelay).*/
airport(toronto, 50, 60).
airport(madrid , 75 , 45).
airport(malaga, 50 , 30).
airport(valencia , 40 , 20).
airport(barcelona , 40, 30).
airport(london , 75, 80).
airport(paris , 50, 60).
airport(toulouse , 40, 30).

/*Below are the facts regarding flights*/
/*flight(name, to, from, price, duration).*/
flight('air canada', toronto, london, 500, 360).
flight(united, toronto, london, 650, 420).
flight(united, toronto, madrid, 950, 540).
flight(iberia, toronto, madrid, 800, 480).
flight('air canada', toronto, madrid, 900, 480).
flight('air canada', madrid, barcelona, 100, 60).
flight(iberia, madrid, barcelona, 120, 65).
flight(iberia, barcelona, london, 220, 240).
flight(iberia, barcelona, valencia, 110, 75).
flight(iberia, madrid, valencia, 40, 50).
flight(iberia, madrid, malaga, 50, 60).
flight(iberia, valencia, malaga, 80, 120).
flight(united, paris, toulouse, 35, 120).

/*Query to print all possible flights in both directions given two cities*/
printFlights(City1, City2) :-
	(flight(Plane, City1, City2, Price, Duration);
	flight(Plane, City1, City2, Price, Duration)),
	printFlight(Plane, City1, City2, Price, Duration),
	printFlight(Plane, City2, City1, Price, Duration).

/*Rules (As per the questions) :*/

/*a. Is there a flight from Toronto to Madrid?
	flightByCity(toronto, madrid). */

flightByCity(A, B) :-
	(flight(Plane, A, B, Price, Duration);
	flight(Plane, B, A, Price, Duration)).

/*b.  A flight from city A to city B with airline C is cheap if its price is less than $400.*/

isCheap(A, B, C) :-
	(flight(C, A, B, Price, Duration);
	flight(C, B, A, Price, Duration)), 
	(Price < 400).

/*c. Is it possible to go from Toronto to Paris in two flights? 
	twoFlights(toronto, paris). */

twoFlights(A, B) :-
	(flightByCity(A, C), flightByCity(C, B));
	(flightByCity(B, C), flightByCity(C, A)).

/*d.A flight from city A to city B with airline C is preferred if it’s cheap (see (b)) or it’s with Air Canada.*/

isPreferred(A, B, C) :-
	isCheap(A, B, C); 
	((C = 'air canada'), (flight('air canada', A, B, D, E); flight('air canada', B, A, D, E))).

/*e.If there is a flight from city A to city B with United, then there is a flight from city A to city B with Air Canada.*/
/* Implies type of statement */

unitedAndAirCanada(A, B) :-
	(\+ (flight(united, A, B, C, D); flight(united, B, A, C, D))); 
	(flight('air canada', A, B, C, D); flight('air canada', B, A, C, D)). 	

/*Flight Display Function*/
printFlight(Plane, City1, City2, Price, Duration):-
	write('\n\nFlight Name:\n'),
   	write(Plane),
	write('\nDeparture From:\n'),
   	write(City1),
   	write('\nArrival To:\n'),
   	write(City2),
   	write('\nPrice:\n'),
   	write(Price),
   	write('\nDuration:\n'),
   	write(Duration).