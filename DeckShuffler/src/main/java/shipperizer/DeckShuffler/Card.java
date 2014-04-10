package shipperizer.DeckShuffler;

public class Card {

	private String suit;
	private int number;
	static private String[] FaceMapper= new String[]{"Jack","Queen","King","Ace"};
	
	public Card(String suit, int number)
		{
		 this.suit= suit;
		 this.number=number;
		}
	
	public String getSuit()
		{ return suit;}
	
	public void setSuit(String suit)
		{ this.suit=suit;}

	public String getNumber()
		{ return displayer(number);}

	public void setNumber(int number)
		{ this.number=number;}

	private String displayer(int number)
	{
	 if(number>10) return FaceMapper[number-11];
	 else return String.valueOf(number);
	}

}