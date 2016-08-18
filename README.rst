Sphinx Document Example
-----------------------

.. code:: bash
  
  # setup
  pip -r requirements/dev.txt

  # auto build for live editing
  make -C sphinx-doc-base livehtml

  # build html
  make -C sphinx-doc-base html
  open sphinx-doc-base/build/html/index.html

