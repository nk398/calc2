from app.controllers.controller import ControllerBase
from flask import render_template

class OOPController(ControllerBase):
    @staticmethod
    def get():
        return render_template('oops_articles.html')

