package com.ChessGUI;

import javax.swing.*;

public class UserInterface extends JFrame {

    ChessBoard chessBoard;

    UserInterface(int width, int height){

        int frameWidth = (int) (width * 1.1);
        int frameHeight = (int) (height * 1.1);

        this.setTitle("Chess");
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setSize(frameWidth, frameHeight);
        this.setResizable(true);
        this.setLayout(null); // decide which layout to use later.

        chessBoard = new ChessBoard(width, height);

        this.add(chessBoard);
        this.setVisible(true);



        // Testing reloading the board multiple times. First one has state string already loaded in.

        chessBoard.reloadPieces(chessBoard.getGameData().getBoardStateString());


        for (int i : ChessPiece.squareNumberPieceMap.keySet()){
            System.out.println(i);
            System.out.println(ChessPiece.squareNumberPieceMap.get(i));
        }


//        String boardStateString = "a1-wr/a2-wp/b1-wk/b2-wp/c1-wb/c2-wp/d1-wQ/d4-wp/e1-wK/e2-wp/f1-wb/f2-wp/g1-wk/g2-wp/h1-wr/h2-wp/a7-bp/a8-br/b7-bp/b8-bk/c7-bp/c8-bb/d7-bp/d8-bQ/e7-bp/e8-bK/f7-bp/f8-bb/g7-bp/g8-bk/h7-bp/h8-br/b-b.c.1-w.c.1-b.ep.0";
//        chessBoard.reloadPieces(boardStateString);
//
//        String boardStateString = "a2-wp/c3-wb/e2-wK/e3-wp/f1-wr/g2-wp/g7-wr/b4-bp/b6-bK/f2-bp/f5-br/h2-bb/h5-bp/w-w.c.0-b.c.0-w.ep.0";
//        chessBoard.reloadPieces(boardStateString);
//
//        boardStateString = "a2-wp/a7-wr/e2-wK/e4-wp/f5-wr/g2-wp/b4-bp/c4-bK/h2-bb/h5-bp/w-w.c.0-b.c.0-w.ep.0";
//        chessBoard.reloadPieces(boardStateString);
//
//        boardStateString = "b7-wr/e3-wK/e7-wp/g2-wp/a2-bK/b2-bp/w-w.c.0-b.c.0-w.ep.0";
//        chessBoard.reloadPieces(boardStateString);


    }

}
