import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class ChessBoard extends JLayeredPane{

    private int boardWidth;
    private int boardHeight;

    JLabel piece;

    ChessBoard(int width, int height){

        this.setBoardWidth(width);
        this.setBoardHeight(height);
        this.setBounds(0, 0, getBoardWidth(), getBoardHeight());

        // prototype linked map data structure mimicking what linked map will be.
        // getting the square colour data as an array of chars.
        GameData gameData = new GameData();

        this.addSquares(gameData.getSquareSymbols());
        this.addPieces(gameData.getPieceSymbols());
        this.addPieceListeners();
        //this.addSquareListeners();

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

                ChessPiece piece = new ChessPiece(pieceSymbols[squareIndex], squareIndex, getBoardWidth(), getBoardHeight());
                this.add(piece.addLabel(), Integer.valueOf(1));

            }
        }
    }

    private void setPaneLayer(Component component, String layer){
        this.setLayer(component, Integer.valueOf(layer));
    }

    private void addPieceListeners(){

        for (Component component : this.getComponents()){
            if (component instanceof JLabel){

                piece = (JLabel) component;
                ChessPiece selectedPiece = (ChessPiece) component;

                selectedPiece.addMouseListener(
                        new MouseListener() {
                            @Override
                            public void mouseClicked(MouseEvent e) {}

                            @Override
                            public void mousePressed(MouseEvent e) {}

                            @Override
                            public void mouseReleased(MouseEvent e) {
                                selectedPiece.movePiece(e, true);
                                setPaneLayer(selectedPiece, "1");
                            }

                            @Override
                            public void mouseEntered(MouseEvent e) {}
                            @Override
                            public void mouseExited(MouseEvent e) {}
                        }
                );

                selectedPiece.addMouseMotionListener(
                        new MouseMotionAdapter() {
                            // whenever the mouse is moved...
                            @Override
                            public void mouseDragged(MouseEvent e) {
                                setPaneLayer(selectedPiece, "2");
                                selectedPiece.movePiece(e, false);
                            }
                        }
                );
            }
        }
    }

    static void highlightPositionSquare(Point position){

        int positionSquareNumber = BoardSquare.calcSquareNumber((int)position.getX(), (int)position.getY());
        BoardSquare square = BoardSquare.squareNumberMap.get(positionSquareNumber);

        // getting the pos marker associated with a square and
        // adding it to the square.
        square.displaySquarePosMarker();
        square.revalidate();
        square.repaint();

        // Have managed to sort out the looping above, however, need to sort this part out.
        for (int i=0; i<64; i++){
            if (i != positionSquareNumber){

                BoardSquare otherSquare = BoardSquare.squareNumberMap.get(i);
                otherSquare.removeSquarePosMarker();
                otherSquare.revalidate();
                otherSquare.repaint();

            }
        }
    }

    // TODO Need to store the last square the mouse was in, so we can
    // TODO remove its label below - this will avoid excessive looping above.
    static void removeHighlightPrevSquare(){
    }

}
