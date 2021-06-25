import javax.swing.*;
import java.awt.*;
import java.util.HashMap;

public class BoardSquare extends JPanel{

    private int squareXPos;
    private int squareYPos;

    private static int boardWidth;
    private static int boardHeight;

    //public static final HashMap<Integer, String> = new HashMap<Integer, String>();

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
