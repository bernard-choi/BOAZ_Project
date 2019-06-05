import tensorflow as tf
from data_utils import *
from rnn_model.attention_lstm import bilstm_with_attention



NUM_CLASS = 30
BATCH_SIZE = 64
NUM_EPOCHS = 1
WORD_MAX_LEN = 50




word_dict = build_word_dict()
vocabulary_size = len(word_dict)
train_x, train_y = build_word_dataset("train", word_dict, WORD_MAX_LEN)
test_x, test_y = build_word_dataset("train", word_dict, WORD_MAX_LEN)

with tf.Session() as sess:

    model = bilstm_with_attention(vocab_size, 50, 30)  ## vocab_size, max_length, class
    init = tf.global_variables_initializer()
    sess.run(init)

    saver = tf.train.Saver(tf.global_variables())

    train_batches = batch_iter(train_x, train_y, BATCH_SIZE, NUM_EPOCHS)
    num_batches_per_epoch = (len(train_x) - 1) // BATCH_SIZE + 1
    max_accuracy = 0

    for x_batch, y_batch in train_batches:
        train_feed_dict = {
            model.x: x_batch,
            model.y: y_batch,
            model.is_training: True
        }

        _, step, loss = sess.run([model.optimizer, model.global_step, model.loss], feed_dict=train_feed_dict)

        if step % 100 == 0:
            print("step {0}: loss = {1}".format(step, loss))

        if (step % 1000 == 0) or (step == num_batches_per_epoch ) :
            # Test accuracy with validation data for each epoch.
            valid_batches = batch_iter(test_x, test_y, BATCH_SIZE, 1) ## test 단에서는 num_epoch 1로 준다
            sum_accuracy, cnt = 0, 0

            for valid_x_batch, valid_y_batch in valid_batches:
                valid_feed_dict = {
                    model.x: valid_x_batch,
                    model.y: valid_y_batch,
                    model.is_training: False
                }

                accuracy = sess.run(model.accuracy, feed_dict=valid_feed_dict)
                sum_accuracy += accuracy
                cnt += 1
            valid_accuracy = sum_accuracy / cnt

            print("\nValidation Accuracy = {1}\n".format(step // num_batches_per_epoch, sum_accuracy / cnt))

            # Save model
            if valid_accuracy > max_accuracy:
                max_accuracy = valid_accuracy
                saver.save(sess, "{0}/{1}.ckpt".format("BILSTM_attention", "BILSTM_attention"), global_step=step)
                print("Model is saved.\n")
