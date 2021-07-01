package com.ChessGUI;

import javax.swing.*;
import java.awt.*;
import java.util.HashMap;

public class BoardSquare extends JPanel{

    static HashMap<Integer, BoardSquare> squareNumberMap = new HashMap<Integer, BoardSquare>();
    private static int squareNumberCounter = 0;
    int squareNumber;

    static Color whiteSquareColour = new Color(238,238,210);
    static Color blackSquareColour = new Color(118,150,86);
    static Color highlightColour = new Color(186,202,68);

    private Color squareColour; // store the underlying square colour

    private int squareXPos;
    private int squareYPos;

    private JLabel squarePosMarker;
    static int lastHighlightedSquareNumber = -1;

    private static int boardWidth;
    private static int boardHeight;

    BoardSquare(char squareSymbol, int squareNumber, int boardWidth, int boardHeight){


        this.boardWidth = boardWidth;
        this.boardHeight = boardHeight;

        // setting the square colour to white or black depending on the
        // square symbol.
        if (squareSymbol == '+'){
            Color squareColour = whiteSquareColour;
            this.setBackground(squareColour);
            this.setSquareColour(squareColour);
        } else if (squareSymbol == '-'){
            Color squareColour = blackSquareColour;
            this.setBackground(squareColour);
            this.setSquareColour(squareColour);
        }

        this.setSquareXPos(squareNumber, boardWidth);
        this.setSquareYPos(squareNumber, boardHeight);
        this.setBounds(getSquareXPos(), getSquareYPos(), boardWidth/8, boardHeight/8);

        //this.setSquarePosMarker(); // initiating the square pos marker -

        // adding the current square to a hashmap with its corresponding square number.
        squareNumberMap.put(squareNumberCounter, this);
        setSquareNumber(squareNumberCounter);
        squareNumberCounter++; // squareNumber goes from 0 --> 63.



    }

    public int getSquareNumber(){
        return this.squareNumber;
    }

    public void setSquareNumber(int squareNumber){
        this.squareNumber = squareNumber;
    }

    public Color getSquareColour(){
        return this.squareColour;
    }

    public void setSquareColour(Color colour){
        this.squareColour = colour;
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
        //this.remove(getSquarePosMarker()); // is there a need to remove first?
//        Border border = BorderFactory.createLineBorder(Color.red,3);
//        getSquarePosMarker().setBorder(border);
//
//
//        this.add(getSquarePosMarker());

        // try simply changing the sq colour.
        this.setBackground(highlightColour);
        this.revalidate();
        this.repaint();

        BoardSquare.lastHighlightedSquareNumber = this.getSquareNumber();

    }

    public void removeSquarePosMarker(){
        this.remove(getSquarePosMarker());
        this.revalidate();
        this.repaint();
    }

    static int calcBoardXPos(int squareNumber, int boardWidth){

        if (!ChessBoard.isRotated){
            return (squareNumber % 8) * (boardWidth / 8);
        } else {
            return BoardSquare.rotateBoardXCoordinate( (squareNumber % 8) * (boardWidth / 8), boardWidth );
        }

    }
    static int calcBoardYPos(int squareNumber, int boardHeight){
        if (!ChessBoard.isRotated) {
            return (squareNumber / 8) * (boardHeight / 8);
        } else {
            return BoardSquare.rotateBoardYCoordinate( (squareNumber / 8) * (boardHeight / 8), boardHeight );
        }
    }

    static int calcSquareNumber(int xPos, int yPos){

        double squareLength = (boardWidth/8);

        double squaresAcross = Math.round(xPos/squareLength);
        double squaresDown = Math.round(yPos/squareLength);

        if (!ChessBoard.isRotated) {
            return (((int) squaresDown) * 8) + (int) squaresAcross;
        } else {
            return BoardSquare.rotateBoardSquareNumber( (((int) squaresDown) * 8) + (int) squaresAcross );
        }

        //return squareNumber;
    }

    static int rotateBoardXCoordinate(int currentXPos, int boardWidth){
        int squareLength = boardWidth/8;
        int newXPos = Math.abs(currentXPos - boardWidth) - squareLength;
        return newXPos;
    }

    static int rotateBoardYCoordinate(int currentYPos, int boardHeight){
        int squareLength = boardHeight/8;
        int newYPos = Math.abs(currentYPos - boardHeight) - squareLength;
        return newYPos;
    }

    static int rotateBoardSquareNumber(int squareNumber){
        return Math.abs(63 - squareNumber);
    }

}
