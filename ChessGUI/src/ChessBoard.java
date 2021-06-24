import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionAdapter;

public class ChessBoard extends JLayeredPane{

    private int boardWidth;
    private int boardHeight;

    JLabel selectedPiece;
    Point pieceCorner;
    Point prevMousePos;

    ChessBoard(int width, int height){


        this.setBoardWidth(width);
        this.setBoardHeight(height);
        this.setBounds(0, 0, getBoardWidth(), getBoardHeight());

        // prototype linked map data structure mimicking what linked map will be.
        // getting the square colour data as an array of chars.
        GameData gameData = new GameData();

        this.addSquares(gameData.getSquareSymbols());
        this.addPieces(gameData.getPieceSymbols());

        for (Component component : this.getComponents()){
            if (component instanceof JLabel){

                selectedPiece = (JLabel) component;
                ChessPiece piece = (ChessPiece) component;

                selectedPiece.addMouseMotionListener(
                        new MouseMotionAdapter() {

                                // whenever the mouse is moved...
                                @Override
                                public void mouseDragged(MouseEvent e) {

                                    // the listener is on the label itself so the coordinate is relative
                                    // to the label.
                                    //
                                    // Therefore we can transform the whole label by the new position after
                                    // dragging as this will always be within the area of the label, so it wont
                                    // jump around.
                                    Point newPos = e.getPoint();
                                    System.out.println(newPos);

                                    Point piecePos = new Point(
                                            (int)piece.getPosition().getX() - (int)getBoardWidth()/16,
                                            (int)piece.getPosition().getY() - (int)getBoardHeight()/16
                                    );

                                    piecePos.translate((int)newPos.getX(), (int)newPos.getY());

                                    piece.setPosition(piecePos);
                                    piece.addLabel();
                            }
                        }
                );

            }
        }
    }

    public int getBoardWidth(){
        return this.boardWidth;
    }
    public void setBoardWidth(int width){
        this.boardWidth = width;
    }
    public int getBoardHeight(){
        return this.boardHeight;
    }
    public void setBoardHeight(int height){
        this.boardHeight = height;
    }

    private void addSquares(char[] squareSymbols){
        for (int i=1; i<=squareSymbols.length; i++){

            int squareIndex = (i-1);
            this.add(
                    new BoardSquare(squareSymbols[squareIndex], squareIndex, this.getBoardWidth(), this.getBoardHeight()),
                    Integer.valueOf(0)
            );
        }
    }

    private void addPieces(char[] pieceSymbols){
        for (int i=1; i<=pieceSymbols.length; i++){
            if (pieceSymbols[i-1] != ' '){

                int squareIndex = i-1;

                ChessPiece piece = new ChessPiece(
                        pieceSymbols[squareIndex], squareIndex, getBoardWidth(), getBoardHeight()
                );

                this.add(piece.addLabel(), Integer.valueOf(1));

            }
        }
    }
}
