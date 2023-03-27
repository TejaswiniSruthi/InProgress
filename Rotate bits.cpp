vector<int>vect;
            vect.push_back(n<<(d%16)&(1<<16)-1)|(1<<(d%16)<<(16-(d%16)));
            vect.push_back(((n&((1<<(d%16))-1))<<(16-(d%16)))|(n>>(d%16)));
            return vect;
