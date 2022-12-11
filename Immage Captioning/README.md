Prova per capire le parti fondamintali di un algoritmo di Immage captioning.
In particolare, capire come creare e maneggaire un Dataset attraverso funzioni custom, per irotrare immagini e didascalie.

Nel progetto si utilizza una struttura di encoder decoder, composta di una Cnn, e come decoder una RNN.

Per poi unire il tutto attraverso una funzione chiamata CNNtoRNN


Il Training set e composto da immagini prese dal dataset flirk8k, e le caption date in un txt, composto come segue ( id_immagine, caption )
Dowland datset https://www.kaggle.com/datasets/adityajn105/flickr8k