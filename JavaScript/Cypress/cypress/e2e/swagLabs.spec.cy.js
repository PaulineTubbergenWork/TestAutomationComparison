describe('Test Swag Labs Website', () => {
    it('tests that I can visit the swag labs website and log in', () => {
        cy.visit('https://www.saucedemo.com/');
        cy.get('input[data-test="username"]').type('standard_user');
        cy.get('input[data-test="password"]').type('secret_sauce');
        cy.get('[data-test="login-button"]').click();

        cy.contains('.primary_header', 'Swag Labs').should('be.visible');
    });
});