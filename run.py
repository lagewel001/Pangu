import logging
import os
import shutil
import sys
from allennlp.commands import main  # pylint: disable=wrong-import-position
# sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir))))
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                    level=logging.INFO)

if __name__ == "__main__":
    if os.path.exists('grailQAbility_results'):
        shutil.rmtree("grailQAbility_results")  # TODO: remove this
    main()