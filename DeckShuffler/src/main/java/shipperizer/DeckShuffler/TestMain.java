package shipperizer.DeckShuffler;

public class TestMain {
	
	public static void main(String args[])
		{
		 DeckShuffler myDeck= new DeckShuffler();
		 myDeck.printDeck();
		 Card A=myDeck.nextCard();
		 System.out.println("Card: "+ A.getNumber() +" of " + A.getSuit());
		 myDeck.printDeck();
		 myDeck.reshuffle();
		 myDeck.printDeck();
		 for(int i=0;i<52;i++)
		 	{
			 A=myDeck.nextCard();
			 System.out.println("Card: "+ A.getNumber() +" of " + A.getSuit());
		 	}
		 myDeck.printDeck();
		 A=myDeck.nextCard();
		 System.out.println("Card: "+ A.getNumber() +" of " + A.getSuit());
		 myDeck.printDeck();
		 
		}
		
	
}
