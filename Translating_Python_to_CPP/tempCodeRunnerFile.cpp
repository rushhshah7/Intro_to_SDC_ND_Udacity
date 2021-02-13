bool test_initialize() {
	vector < vector <char> > map;
	map = read_map("maps/m1.txt");
	vector < vector <float> > beliefs, correct;
	beliefs = initialize_beliefs(map);

	int h, w, A; 
	float belief;

	h = map.size();

	if (h < 1) {
		cout << "failed to load map. Make sure there is a maps/ directory in the same directory as this file!\n";
		return false;
	}
	w = map[0].size();
	A = h * w;
	belief = 1.0 / A;



	int i, j;
	vector <float> row;
	for (i=0; i<map.size(); i++) {
		row.clear();
		for (j=0; j<map[0].size(); j++) {
			row.push_back(belief);
		}
		correct.push_back(row);
	}

	bool right = close_enough(correct, beliefs);

	if (right) {
		cout << "! - initialize_beliefs function worked correctly!\n";
	}
	else {
		cout << "X - initialize_beliefs function did not work correctly.\n";
		cout << "For the following input:\n\n";
		show_grid(map);
		cout << "\nYour code returned the following:\n\n";
		show_grid(beliefs);
		cout << "\nWhen it should have returned the following:\n";
		show_grid(correct);
	}

	return right;

}