$(document).ready(function() {
    $('#load-pantry').click(function() {
        $.ajax({
             url: '/api/pantry/items/',  // Убедитесь, что URL правильный
            method: 'GET',
            headers: {
                'Authorization': 'Token 5f1421267e5d27897a529bee99d4ba6d9040e132'
            },
            success: function(data) {
                $('#pantry-items').empty(); // Очистка контейнера перед добавлением новых элементов
                if (data.length === 0) {
                    $('#pantry-items').append('<p>No items in pantry</p>');
                } else {
                    data.forEach(function(item) {
                        $('#pantry-items').append(`
                            <div class="card mt-3">
                                <div class="card-body">
                                    <h5 class="card-title">${item.name}</h5>
                                    <p class="card-text">Quantity: ${item.quantity} ${item.unit}</p>
                                </div>
                            </div>
                        `);
                    });
                }
            },
            error: function(error) {
                console.error('Error loading pantry items:', error);
            }
        });
    });
});