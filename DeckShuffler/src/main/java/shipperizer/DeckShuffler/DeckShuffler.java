package shipperizer.DeckShuffler;


public class DeckShuffler {

	static private String[] SuitsMapper= new String[]{"Spades","Clubs","Hearts","Diamonds"};
	
	private Card[] Deck=null;
	private int cDeck;
	public DeckShuffler()
		{
		 Deck=new Card[52];
		 cDeck=51;
		 for(int suit=0;suit<4;suit++)
			{
			 for(int card=0;card<13;card++)
				 {
				  Deck[(suit*13)+card]=new Card(SuitsMapper[suit],card+1);//cards number go from 1 to 14 (1 to Ace)
				  System.out.println("Card: "+((suit*13)+card));
				 }
			}
		 reshuffle(false);
		}
	
	public Card nextCard()
		{
		 if(cDeck==-1) reshuffle();
		 cDeck--;
		 return Deck[cDeck+1];
		}
	
	public void reshuffle()
		{
		 reshuffle(true);		 
		}
	
	public void printDeck()
		{
     	 System.out.println("----------------------------------------------------------------------------");
		 System.out.println("Playing Deck");
		 for(int i=0;i<=cDeck;i++)
			 System.out.println("Card-"+i+": "+ Deck[i].getNumber()+" of " + Deck[i].getSuit());
		 System.out.println("----------------------------------------------------------------------------");
		}
	
	private void reshuffle(boolean Public)
		{
		 cDeck=51;
		 Card tmp=null;
		 int tmpIndex;
		 for(int i=0;i<4;i++)
			 for(int h=0;h<52;h++)
				 {
				  tmpIndex=(int)(Math.random()*52)%52;
				  tmp = Deck[h];
				  Deck[h]=Deck[tmpIndex];
				  Deck[tmpIndex]=tmp;
				 }
		}
	
	
}
