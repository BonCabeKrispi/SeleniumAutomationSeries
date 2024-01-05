/// <reference types="cypress" />


describe('Login dashboard', () => {
    
      //viewport in cypress
      it('login page with auth', ()=> {
        //the size of the windows
        cy.viewport(1280, 720)
        cy.clearCookies()
        //link of the websites
        cy.visit('http:')
        //input id of the field
        cy.get('Id of the field username').type('username')
        //case when the check the username need to clicked button 
        //read the name of the button
        cy.contains('Login').click()
        //if the field noneed to check the username, skip the contain login part.
        cy.get('id of the field password').type('password')
        cy.contains('Login').click()  

    })   

})
