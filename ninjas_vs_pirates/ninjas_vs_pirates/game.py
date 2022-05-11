from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

michelangelo.attack(jack_sparrow)
jack_sparrow.show_stats()

jack_sparrow.attack(michelangelo)
michelangelo.show_stats()