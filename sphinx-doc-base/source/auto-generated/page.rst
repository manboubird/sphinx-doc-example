Auto Generated Page
-------------------

.. jinja:: tpl_file_params 
   :file: source/j2_templates/user-list.j2
   :header_char: =

.. jinja:: raw_tpl

   Users (raw_tpl)
   ===============
   
   {% for user in users %}
   {% if user.is_active %}
   * `{{ user.name }} <{{ user.url }}>`_
   {% else %}
   * {{ user.name }} (Empty)
   {% endif %}
   {% endfor %}

   List-table
   ^^^^^^^^^^

   .. list-table:: 

    * - head1
      - head2
    * - test1
      - test2

