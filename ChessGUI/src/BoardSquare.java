import javax.swing.*;
import javax.swing.border.Border;
import java.awt.*;

public class BoardSquare extends JPanel{

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

        JLabel marker = new JLabel();
        Border border = BorderFactory.createLineBorder(Color.red,3);
        marker.setText("     "); // ******** Need to work out how to apply to label w/o text.
        marker.setBorder(border);
        marker.setVerticalAlignment(JLabel.CENTER);
        marker.setHorizontalAlignment(JLabel.CENTER);
        marker.setFont(new Font("Ariel", Font.BOLD, 50));
        marker.setForeground(new Color(0xFFFF00)); // yellow
        marker.setBounds(0, 0, boardWidth / 8, boardHeight / 8);
        this.squarePosMarker = marker;
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
