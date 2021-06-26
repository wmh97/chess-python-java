public class GameData {

    private char[] squareSymbols;
    private String[] pieceSymbols;

    GameData(){

        // temp way of generating the data structures that we need to set up the board.

        char[] squareSymbols = new char[64];
        char tempSymbol;
        char symbol1 = '-';
        char symbol2 = '+';
        int fileNumber = 1;

        for (int i=1; i<=64; i++){

            fileNumber++;

            if (i % 2 == 0 ){
                squareSymbols[i-1] = symbol1;
            } else {
                squareSymbols[i-1] = symbol2;
            }

            // swap the symbol characters every row. Won't need this when
            // we are reading symbols from the linked map.
            if (fileNumber > 8){
                tempSymbol = symbol2;
                symbol2 = symbol1;
                symbol1 = tempSymbol;
                fileNumber = 1;
            }

        }

        String[] pieceSymbols = new String[64];

        char[] colours = {'b', 'w'};
        char[] pieces = {'r', 'k', 'b', 'Q', 'K', 'b', 'k', 'r', 'p'};
        String[] colourPieces = new String[18];

        int colourPiecesCounter = 0;
        for (int j=0; j<colours.length; j++){
            for (int k=0; k<pieces.length; k++){
                colourPieces[colourPiecesCounter] = String.valueOf(colours[j]) + String.valueOf(pieces[k]);
                colourPiecesCounter++;
            }
        }

        for (String s: colourPieces){
            System.out.println(s);
        }

        int whiteBackRowIndex = 9;
        for (int i=0; i<64; i++){

            if (i <= 8){
                pieceSymbols[i] = colourPieces[i];
            } else if (i > 8 && i < 16){
                pieceSymbols[i] = colourPieces[8];
            } else if (i >= 48 && i < 56){
                pieceSymbols[i] = colourPieces[17];
            } else if (i >= 56){
                // 9 --> 16
                pieceSymbols[i] = colourPieces[whiteBackRowIndex];
                whiteBackRowIndex++;
            } else{
                pieceSymbols[i] = "";
            }

        }

        for (String s: pieceSymbols){
            System.out.println(s);
        }


        setSquareSymbols(squareSymbols);
        setPieceSymbols(pieceSymbols);

    }

    public char[] getSquareSymbols(){
        return this.squareSymbols;
    }

    public void setSquareSymbols(char[] squareSymbols){
        this.squareSymbols = squareSymbols;
    }

    public String[] getPieceSymbols(){
        return this.pieceSymbols;
    }

    public void setPieceSymbols(String[] pieceSymbols){
        this.pieceSymbols = pieceSymbols;
    }

}
