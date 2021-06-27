package com.ChessGUI;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.File;
import java.io.IOException;

public class GameData {

    private char[] squareSymbols;
    private String[] pieceSymbols;
    private String boardStateString;

    private static final ObjectMapper objectMapper = new ObjectMapper();

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

        setSquareSymbols(squareSymbols);
        setPieceSymbols(pieceSymbols);



        /////////////////////////////////

        try {

            String projectDir = System.getProperty("user.dir").replace("\\ChessGUI", "");
            JsonNode gameJson = objectMapper.readTree(
                    new File(String.format("%s\\game_json.json", projectDir))
            );

            String boardStateString = gameJson.path("Controller.CURRENT_POSITION_STRING").asText();
            setBoardStateString(boardStateString);

            System.out.println(getBoardStateString());

        } catch (IOException e) {
            e.printStackTrace();
        }


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

    public String getBoardStateString(){
        return this.boardStateString;
    }

    public void setBoardStateString(String boardStateString){
        this.boardStateString = boardStateString;
    }

}
