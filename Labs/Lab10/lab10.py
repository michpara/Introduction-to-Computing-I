import math
class Point:
    'class that represents a point in the plane'

## exectuting Point(2,3)
## 1. creates an object of type point
## 2. calls an objects __init__ method
## 3. produces an object's memory address

## Assigning to a new variable using dot operator
## CREATES THAT VARIABLE INSIDE OF THE OBJECT

## Variables INSIDE of an object are called INSTANCE variables

## __init__ is method that is called to initialize the object (create it and initialize its variables)
## the first parameter of method is usually called self
## self refers to the object that is being initialized


#    constructor
#    notice two underscores
    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point, float, float) -> None
        >>> p=Point(2,3)
        >>> p.x
        >>> 2
        >>> p.y
        >>> 3

        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,float)->None
        set x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,float)->None
        set y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        return a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,float,float)->None
        change the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        'self == other if they have the same coordinates'
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        'return canonical string representation Point(x, y)'
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def distance(self,other):
        """(Point, Point) -> float
        Returns the distance between two point
        """
        return math.sqrt((self.x - other.x)**2 +(self.y - other.y)**2)
    def up(self):
        """(Point) -> None
        Moves Point up by 1
        """
        self.move(0, 1)
    def down(self):
        """(Point) -> None
        Moves Point down by 1
        """
        self.move(0,-1)
    def left(self):
        """(Point) -> None
        Moves Point left by 1
        """
        self.move(-1, 0)
    def right(self):
        """(Point) -> None
        Moves Point right by 1
        """
        self.move(1,0)
class Animal:
    'represents an animal'

    def __init__(self, species='animal', language='make sounds', age = 0):
        self.spec = species
        self.lang = language
        self.age = age

    def setSpecies(self, species):
        'sets the animal species'
        self.spec = species

    def setLanguage(self, language):
        'sets the animal language'
        self.lang = language

    def speak(self):
        'prints a sentence by the animal'
        print('I am a', self.spec,'and I', self.lang)
    
    def getAge(self):
        """(Animal) -> int
        Returns age of the animal.
        """
        return self.age
class Bird(Animal): # class Bird inherits all atributes (data and method) from class Animal 
    'represents a bird'

    def speak(self):
        'prints bird sounds'
        print(self.language * 3)



class Card:
    'represents a playing card'

    def __init__(self, rank, suit):
        'initialize rank and suit of card'
        self.rank = rank
        self.suit = suit

    def getRank(self):
        'return rank'
        return self.rank

    def getSuit(self):
        'return suit'
        return self.suit    

    def __repr__(self):
        'return formal representation'
        return 'Card('+self.rank+','+self.suit+')'

    def __eq__(self, other):
        'self == other if rank and suit are the same'
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        """(Card, Card) -> bool
            Return True if the rank of the card on the left,self
            is less than the rank of the card compared with it, other.
            Otherwise False
        """
        return int(self.rank) < int(other.rank)

    def __le__(self, other):
        """(Card, Card) -> bool
            Return True if the rank of the card on the left,self
            is less than or equal to the rank of the card compared with it, other.
            Otherwise False
        """
        return int(self.rank) <= int(other.rank)
        
    def __gt__(self, other):
        """(Card, Card) -> bool
            Return True if the rank of the card on the left,self
            is greater than the rank of the card compared with it, other.
            Otherwise False
        """
        return int(self.rank) > int(other.rank)

    def __ge__(self, other):
        """(Card, Card) -> bool
            Return True if the rank of the card on the left,self
            is greater than or equal to the rank of the card compared with it, other.
            Otherwise False
        """
        return int(self.rank) >= int(other.rank)
class Deck:
    'represents a deck of 52 cards'

    # ranks and suits are Deck class variables
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    # suits is a set of 4 Unicode symbols representing the 4 suits 
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self):
        'initialize deck of 52 cards'
        self.deck = []          # deck is initially empty

        for suit in Deck.suits: # suits and ranks are Deck
            for rank in Deck.ranks: # class variables
                # add Card with given rank and suit to deck
                self.deck.append(Card(rank,suit))

    def dealCard(self):
        'deal (pop and return) card from the top of the deck'
        return self.deck.pop()

    def shuffle(self):
        'shuffle the deck'
        random.shuffle(self.deck)


    def __len__(self):
        'returns size of deck'
        return len(self.deck)

    def __repr__(self):
        'returns canonical string representation'
        return 'Deck('+str(self.deck)+')'

    def __eq__(self, other):
        '''returns True if decks have the same cards
           in the same order'''
        return self.deck == other.deck

class Vector(Point):
    '''class that represents a Vector'''
    
    def __init__(self, xcoord=0, ycoord=0):
        '''(Vector, Number, Number)->None'''
        self.x = xcoord
        self.y = ycoord

    def __add__(self, other):
        '''(Vector, Vector)->Vector
        adds to vectors together''' 
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        '''(Vector, Vector)->Integer
        returns the cross value of two vectors'''
        return self.x*other.x + self.y*other.y

    def __repr__(self):
        '''(Vector)->String
        formal representation of Vector'''
        return 'Vector(' + str(self.x) + ',' + str(self.y) + ')'

class Points(Point):
    '''class representing points'''
    
    def __init__(self, points = []):
        '''(Points, List)->None'''
        self.points = points

    def add(self, x, y):
        '''(Points, Number, Number)->()
        adds a point with coordinates x and y to points'''
        self.points.append(Point(x, y))

    def left_most_point(self):
        '''(Points)->Point
        returns the point with the left most value and the lowest value'''
        left_most = self.points[0]
        for i in self.points:
            if left_most.x > i.x:   
                left_most = i
            elif left_most.x == i.x and left_most.y > i.y:
                left_most = i
        return left_most
            

    def __len__(self):
        '''(Points)->Integer
        returns the length of points'''
        return len(self.points)

    def __repr__(self):
        '''(Points)->String
        formal representation of points'''
        return 'Points(' + str(self.points) + ')'
