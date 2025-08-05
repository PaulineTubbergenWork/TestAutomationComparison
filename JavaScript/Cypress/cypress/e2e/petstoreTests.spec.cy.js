describe('Petstore tests', () => {
    it('checks that I can visit the petstore', () => {
        cy.visit('https://petstore.octoperf.com/');
        cy.contains('a', 'Enter the Store').click();
        cy.get('#MainImage').should('be.visible');
        cy.get('#MainImage area[alt="Reptiles"]').click();
        cy.get('#Catalog h2').should('have.text', 'Reptiles').and('be.visible');
    });
});
