import javax.swing.*;
import javax.swing.border.Border;
import java.awt.*;
import java.util.HashMap;

public class BoardSquare extends JPanel{

    static HashMap<Integer, BoardSquare> squareNumberMap = new HashMap<Integer, BoardSquare>();
    private static int squareNumber = 0;

    private int squareXPos;
    private int squareYPos;

    private JLabel squarePosMarker;

    private static int boardWidth;
    private static int boardHeight;

    BoardSquare(char squareSymbol, int squareNumber, int boardWidth, int boardHeight){


        this.boardWidth = boardWidth;
        this.boardHeight = boardHeight;

        // setting the square colour to white or black depending on the
        // square symbol.
        if (squareSymbol == '+'){
            this.setBackground(Color.white);
        } else if (squareSymbol == '-'){
            this.setBackground(Color.black);
        }

        this.setSquareXPos(squareNumber, boardWidth);
        this.setSquareYPos(squareNumber, boardHeight);
        this.setBounds(getSquareXPos(), getSquareYPos(), boardWidth/8, boardHeight/8);

        this.setSquarePosMarker(); // initiating the square pos marker but not adding yet.

        // adding the current square to a hashmap with its corresponding square number.
        squareNumberMap.put(squareNumber, this);
        squareNumber++; // squareNumber goes from 0 --> 63.
    }

    public int getSquareXPos(){
        return this.squareXPos;
    }

    public void setSquareXPos(int squareNumber, int boardWidth){
        this.squareXPos = BoardSquare.calcBoardXPos(squareNumber, boardWidth);
    }

    public int getSquareYPos(){
        return this.squareYPos;
    }

    public void setSquareYPos(int squareNumber, int boardHeight){
        this.squareYPos = BoardSquare.calcBoardYPos(squareNumber, boardHeight);
    }

    public JLabel getSquarePosMarker(){
        return this.squarePosMarker;
    }

    public void setSquarePosMarker(){
        squarePosMarker = new JLabel();
        squarePosMarker.setText("     "); // ******** Need to work out how to apply to label w/o text.
        squarePosMarker.setVerticalAlignment(JLabel.CENTER);
        squarePosMarker.setHorizontalAlignment(JLabel.CENTER);
        squarePosMarker.setFont(new Font("Ariel", Font.BOLD, 50));
        squarePosMarker.setForeground(new Color(0xFFFF00)); // yellow
        squarePosMarker.setBounds(0, 0, boardWidth / 8, boardHeight / 8);
        this.add(squarePosMarker);
    }

    public void displaySquarePosMarker(){
        // re-adding the label to the panel after creating a border on it
        // to represent the highlighting.
        this.remove(getSquarePosMarker()); // is there a need to remove first?
        Border border = BorderFactory.createLineBorder(Color.red,3);
        getSquarePosMarker().setBorder(border);
        this.add(getSquarePosMarker());
    }

    public void removeSquarePosMarker(){
        this.remove(getSquarePosMarker());
        this.revalidate();
        this.repaint();
    }

    static int calcBoardXPos(int squareNumber, int boardWidth){
        return (squareNumber % 8) * (boardWidth / 8);
    }
    static int calcBoardYPos(int squareNumber, int boardHeight){
        return (squareNumber / 8) * (boardHeight / 8);
    }

    static int calcSquareNumber(int xPos, int yPos){

        double squarelength = (boardWidth/8);

        double squaresAcross = Math.round(xPos/squarelength);
        double squaresDown = Math.round(yPos/squarelength);

        int squareNumber = (((int)squaresDown) * 8) + (int)squaresAcross;

        return squareNumber;
    }

}
