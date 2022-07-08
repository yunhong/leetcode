class Solution {
public:
    //vector<vector<char> > board;
    void solveSudoku(vector<vector<char> > &board) {
        //this->board = board;
        DFS(board); 
    }

    bool DFS(vector<vector<char> > &board){
        vector<pair<int, int> > empty_nodes = get_empty_nodes(board);
        if(empty_nodes.empty()) return true;
        
        int min_size = 10;
        pair<int, int> min_node;
        vector<int> min_candidates;
        
        for(pair<int, int> node : empty_nodes){
            int i = node.first, j = node.second;
            vector<int> candidates = get_candidates(node, board);
            if(candidates.empty()) return false;
            if(min_size > candidates.size()){
                min_size = candidates.size();
                min_node = node;
                min_candidates = candidates;
            }  
        }
    
        int i=min_node.first, j = min_node.second;
        for(int v : min_candidates){
            board[i][j] = '0' + v;
            if(DFS(board)) return true;
        }
        board[i][j] = '.';
        return false;
    }
            
    vector<int> get_candidates(pair<int, int> &node, vector<vector<char> > &board){
        int i0 = node.first, j0 = node.second;
        //vector<pair<int, int> > pos24;
        bool flags[9]; 
        for(int i=0; i<9; i++) flags[i] = true;
        
        for(int i=0; i<9; i++){
            if( (i != i0) and (board[i][j0] != '.')){
                char c = board[i][j0];
                int v = c - '1';
                flags[v] = false;
            }
        }
        
        for(int j=0; j<9; j++){
            if( (j != j0) and (board[i0][j] != '.') ){
                char c = board[i0][j];
                int v = c - '1';
                flags[v] = false;
            } 
        }
        
        int I0 = 3 * (int)(i0/3);
        int J0 = 3 * (int)(j0/3);
        for(int i=I0; i<I0+3; i++){
            for(int j=J0; j<J0+3; j++){
                if( ((i != i0) || (j != j0)) and (board[i][j] != '.') ){
                    char c = board[i][j];
                    int v = c - '1';
                    flags[v] = false;
                }
            } // j
        } // i
        
        vector<int> candidates;
        for(int v=0; v<9; v++){
            if(flags[v]) candidates.push_back(v+1);
        }
        return candidates;
    }
    
    vector<pair<int, int> > get_empty_nodes(vector<vector<char> > &board){
        vector<pair<int, int> > empty_nodes;
        for(int i=0; i<9; i++){
            for(int j=0; j<9; j++){
                if(board[i][j] == '.')
                    empty_nodes.push_back(pair<int, int>(i, j));
            }
        }
        return empty_nodes;
    }
};
